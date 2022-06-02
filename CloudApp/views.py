import smtplib
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from.models import UserCreationForm, User
from .forms import FileForm
from .models import File
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='login')
def My_Files(request):
       return render(request, 'home/My Files.html')


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            request.session.set_expiry(86400)
            login(request, user)
            return redirect('my_files')
        else:
            messages.error(request,"Wrong Username Or Password")
    return render(request,'accounts/login.html')

def RegisterPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            global Gform
            global Gemail
            Gform = form
            Gemail = str(form.cleaned_data.get('email'))
            global Code
            Code = str(EmailVerify(Gemail))
            return redirect('verification')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def LoginPageAfterPC(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            request.session.set_expiry(86400)
            login(request, user)
            return redirect('my_files')
        else:
            messages.error(request,"Wrong Username Or Password")

    messages.success(request, "Password Changed for " + request.user.username + " Succesfully")
    return render(request,'accounts/login.html')

def Verification(request):
    if request.method == "POST":
        Mail = str(request.POST.get('email'))
        code = str(request.POST.get('code'))
        if code == Code and Mail == Gemail:
            Gform.save()
            user = Gform.cleaned_data.get('username')
            messages.success(request, "Account Created for " + user + " Succesfully" )
            return redirect('login')
        else:
            messages.error(request, "Wrong Code Or Email.")
    return render(request, 'accounts/Verification.html')

def Admin(request):
    return HttpResponseRedirect(reverse('admin:index'))

@login_required(login_url='login')
def Profile(request):
    return render(request, 'home/profile.html', {'name' : request.user.first_name })

@login_required(login_url='login')
def Upload_File(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.Uploaded_By = request.user.username
            obj.File_Size = Size_Converter(obj.File.size)
            obj.File_Name = obj.File.name
            obj.save()
            return redirect('my_files')
    else:
        form = FileForm()
    return render(request, 'home/Upload_File.html', {'form': form})

@login_required(login_url='login')
def My_Files(request):
    files = File.objects.all()
    return render(request, 'home/My Files.html', {"files" : files})


@login_required(login_url='login')
def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
        return redirect('my_files')


def EmailVerify(email):
    EMAIL_ADDRESS = 'fileme.management@gmail.com'
    EMAIL_PASSWORD = 'FileMeYotam'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        mail_input = Gemail
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        a = random.randint(1000, 10000)
        subject = 'File-Me Verification Code'
        body = "Verification Code: " + str(a) + "\nDon't Share With Anyone."
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, mail_input, msg)
        return a


@csrf_exempt
def Delete_Account(request):
    u = User.objects.get(username=request.user.username)
    u.delete()
    return redirect('my_files')

def logout_user(request):
    auth.logout(request)
    return redirect('my_files')


def Size_Converter(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return str(str(round(size,2)) + " " + str(power_labels[n]))