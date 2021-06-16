from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction









class RecordAddForm(forms.ModelForm):
    courseTitle = forms.CharField(
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label = "*Course Title",
    )

    courseTopic = forms.CharField(
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label = "*Course Topic",
    )
    owner = forms.CharField(
        max_length=300,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',


            }
        ),
        label = "*Current User",

    )

    # courseUnit = forms.CharField(
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     ),
    #     label = "*Course Unit",
    # )

    description = forms.CharField(
        max_length=50000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        label = "Add a little description",
        required = False,
    )

    # level = forms.CharField(
    #     widget=forms.Select(
    #         choices = LEVEL,
    #         attrs={
    #             'class': 'browser-default custom-select',
    #         }
    #     ),
    #     label = "*Level",
    # )

    # semester = forms.CharField(
    #     max_length=30,
    #     widget=forms.Select(
    #         choices=SEMESTER,
    #         attrs={
    #             'class': 'form-control',
    #         }
    #     ),
    #     label = "*Semester",
    # )

    is_reviewed = forms.BooleanField(label = "*is_reviewed", required=False)
    class Meta:
        model = Record
        fields = ['courseTopic', 'courseTitle', 'description','is_reviewed']

