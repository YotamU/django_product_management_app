from django.urls import path
from. import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.My_Files),
    path("Login", views.LoginPage, name="login"),
    path("Logout", views.logout_user, name="Logout"),
    path("Register", views.RegisterPage,name="register"),
    path("admin", views.Admin, name="admin"),
    path("MyFiles", views.My_Files, name="my_files"),
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin/', admin.site.urls),
    path("Profile", views.Profile, name="profile"),
    path("UploadFile", views.Upload_File, name="upload_file"),
    path("MyFiles/<int:pk>/", views.delete_file, name="delete_file"),
    path("Verification", views.Verification,name = "verification"),
    path("Delete", views.Delete_Account,name = "delete_account"),
    path("ChangePassword/", auth_views.PasswordChangeView.as_view(template_name='accounts/ChangePassword.html',success_url="Login"), name="password_change"),
    path("ChangePassword/Login", views.LoginPageAfterPC, name="pass"),



]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)