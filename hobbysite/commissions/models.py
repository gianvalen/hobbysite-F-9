from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from user_management.models import Profile


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    OPEN="1"
    FULL="2"
    COMPLETED="3"
    DISCONTINUED="4"
    STATUS_CHOICES = {
        OPEN: 'Open',
        FULL: 'Full',
        COMPLETED: 'Completed',
        DISCONTINUED: 'Discontinued',
    }   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[OPEN])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='author'
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission-detail', args=[self.pk])
    
    class Meta:
        ordering = ['created_on']


class Job(models.Model):
    commission = models.ForeignKey(
        'Commission', 
        on_delete=models.CASCADE, 
        related_name = 'jobs'
    )
    role = models.CharField(max_length=255)
    manpower_required = models.IntegerField()
    OPEN="1"
    FULL="2"
    STATUS_CHOICES = {
        OPEN: 'Open',
        FULL: 'Full',
    }
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[OPEN])

    def __str__(self):
        return self.role
    
    class Meta:
        ordering = ['status', '-manpower_required', 'role']


class JobApplication(models.Model): 
    job = models.ForeignKey(
        Job, 
        on_delete=models.CASCADE,
        related_name = 'job_application'
    )
    applicant = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE,
        related_name = 'job_application'
    )
    PENDING="1"
    ACCEPTED="2"
    REJECTED="3 "
    STATUS_CHOICES = {
        PENDING: 'Pending',
        ACCEPTED: 'Accepted',
        REJECTED: 'Rejected',
    }
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[PENDING])
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', '-applied_on']