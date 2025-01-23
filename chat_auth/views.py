from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ForgotPasswordForm, ChangePasswordForm
from .middlewares import auth, guest
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

@guest
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                # Send password reset email
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(str(user.pk).encode())
                reset_link = request.build_absolute_uri(f'/reset-password/{uid}/{token}/')

                subject = "Password Reset Instructions"
                message = f"Click the link below to reset your password:\n{reset_link}"
                send_mail(subject, message, 'no-reply@yourdomain.com', [email])

                # Add a success message
                messages.success(request, "An email has been sent with reset instructions.")

            return redirect('forgot_password')  # Reload the page after sending the email
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'change_password.html', {'form': form})