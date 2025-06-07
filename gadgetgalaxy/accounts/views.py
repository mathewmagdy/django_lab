from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import RegisterForm
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.http import HttpResponse

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Wait for email verification
            user.save()

            # Send verification email
            verification_link = request.build_absolute_uri(f"/accounts/verify/{user.activation_token}/")
            send_mail(
                subject="Activate Your Account",
                message=f"Click the link to activate: {verification_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return HttpResponse("Check your email to activate your account.")
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def verify_email(request, token):
    try:
        user = CustomUser.objects.get(activation_token=token)
        if timezone.now() > user.activation_expiry:
            return HttpResponse("Token expired.")
        user.is_active = True
        user.activation_token = None
        user.save()
        return HttpResponse("Your account is activated.")
    except CustomUser.DoesNotExist:
        return HttpResponse("Invalid token.")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('product_list')  # change as needed
        return HttpResponse("Invalid credentials or inactive account.")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
