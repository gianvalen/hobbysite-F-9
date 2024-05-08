from django.shortcuts import redirect, render
from django.db.models import Sum
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Commission, Job
from .forms import CommissionForm, CommissionUpdateForm, JobApplicationForm, JobInlineFormSet
from user_management.models import Profile


def commission_list(request):
    ctx = {
        "commissions_all": Commission.objects.all().order_by('status','-created_on'),
        "commissions_created": Commission.objects.filter(author__user__pk=request.user.pk).order_by('status','-created_on'),
        "commissions_applied_to": Commission.objects.filter(jobs__job_application__applicant=request.user.profile).order_by('status','-created_on'),
    }
    return render(request, "commission_list.html", ctx)


class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = "commission_detail.html"
    context_object_name = 'commission'

    def get_current_user(self):
        user = Profile.objects.get(user=self.request.user)
        return user
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        commission = self.get_object()
        jobs = commission.jobs.all()

        sum_manpower_required = commission.jobs.aggregate(total_manpower_required=Sum('manpower_required'))['total_manpower_required'] or 0
        accepted_job_applications = commission.jobs.filter(job_application__status='Accepted').count()
        open_manpower = sum_manpower_required - accepted_job_applications

        ctx['sum_manpower_required'] = sum_manpower_required
        ctx['open_manpower'] = open_manpower

        ctx['jobs'] = jobs
        ctx['job_application_form'] = JobApplicationForm()

        return ctx

    def post(self, request, *args, **kwargs):
        commission = self.get_object()
        job_application_form = JobApplicationForm(request.POST)
        if job_application_form.is_valid():
            job_application = job_application_form.save(commit=False)
            job_application.commission = commission
            job_application.applicant = self.get_current_user()
            job_pk = request.POST.get('job')
            if job_pk:
                job = Job.objects.get(pk=job_pk)
                job_application.job = job
                job.manpower_required -= 1
                job.save()
                job_application.save()
                return redirect(reverse('commissions:commission-detail', args=[commission.pk]))
        ctx = self.get_context_data()
        ctx['job_application_form'] = job_application_form
        return self.render_to_response(ctx)


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commission_create.html'

    def get_initial(self):
        author = Profile.objects.get(user=self.request.user)
        return {'author':author}
    
    def get_current_user(self):
        user = Profile.objects.get(user=self.request.user)
        return user
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.POST:
            ctx['job_formset'] = JobInlineFormSet(self.request.POST)
        else:
            ctx['job_formset'] = JobInlineFormSet()
        return ctx
    
    def form_valid(self, form):
        ctx = self.get_context_data()
        job_formset = ctx['job_formset']
        
        if job_formset.is_valid():
            self.object = form.save()
            job_formset.instance = self.object
            job_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('commissions:commission-detail', kwargs={'pk': self.object.pk})


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionUpdateForm
    template_name = 'commission_update.html'

    def form_valid(self, form):
        commission = form.save(commit=False)
        all_jobs_full = all(job.status == 'Full' for job in commission.jobs.all())
        if all_jobs_full:
            commission.status = 'Full'
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('commissions:commission-detail', kwargs={'pk': self.object.pk})