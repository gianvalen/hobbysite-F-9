from django import forms
from django.forms import inlineformset_factory

from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'
        widgets = {
            'status': forms.Select(choices=Commission.STATUS_CHOICES),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].disabled = True


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']

JobInlineFormSet = inlineformset_factory(
    Commission, Job, form=JobForm, extra=5, can_delete=True
)


class CommissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'
        exclude = ['created_on', 'author']


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'