from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from php_programmer.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Textarea, CharField, TextInput, Select, NumberInput, PasswordInput, FileInput, FileField

class UploadCSVFileForm(ModelForm):
    file = FileInput(
        attrs={
            'class': 'form_input',
            'placeholder': 'Загрузить данные',
            'required': False
        })

# class FileForm(ModelForm):
#     class Meta:
#         model = File
#         fields = ['file', ]


# class MultiFileForm(forms.ModelForm):
#     files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
#     class Meta:
#         model = File
#         fields = ('file', )

