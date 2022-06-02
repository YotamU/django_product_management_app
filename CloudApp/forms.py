from .models import File
from django import forms
from django.contrib.auth.models import User

# Create your forms here.

class FileForm(forms.ModelForm):
    class Meta:
        model= File
        fields= ["File_Name", "File_Type","Uploaded_By","File_Size","Password","File"]