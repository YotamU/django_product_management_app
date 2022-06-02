from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class File(models.Model):
    File_Name = models.CharField(max_length=200,default=None,blank=True, null=True)
    File_Type = models.CharField(max_length=30, null=True)
    Uploaded_By = models.CharField(max_length=90,default=None,blank=True, null=True)
    File_Size = models.CharField(max_length=1000, default=None,blank=True, null=True)
    Password = models.CharField(max_length=100, null=True)
    File = models.FileField(upload_to='Files')

    def __str__(self):
        return self.File_Name

    def delete(self, *args, **kwargs):
        self.File.delete()
        super().delete(*args, **kwargs)

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user