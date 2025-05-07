from django.shortcuts import render, redirect
# Here, instead of 'User' we want to import 'Custom user model'
from django.contrib.auth import get_user_model, login
from .emailer import sendOTPToEmail
import random
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Customized user model
User = get_user_model()



# Sending an email by logging in with phone number (with extended abstractuser which contains his email)
def login_page(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        user_obj = User.objects.filter(phone_number = phone_number)
        if not user_obj.exists():
            return redirect('/')
        
        email = user_obj[0].email
        otp = random.randint(1000, 9999)

        user_obj.update(otp = otp)

        subject = "Otp for Login"
        message = f"Your OTP is {otp}"

        sendOTPToEmail(
            email, subject, message
        )
        
        return redirect(f'/check_otp/{user_obj[0].id}/')

    return render(request, 'login.html')



def check_otp(request, user_id):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user_obj = User.objects.get(id = user_id)

        if int(otp) == user_obj.otp:
            login(request, user_obj)
            return redirect('/dashboard/')

        # Message error for wrong otp
        messages.error(request, "Invalid OTP")
        
        return redirect(f'/check_otp/{user_obj.id}/')
    
    return render(request, 'check_otp.html')


@login_required(login_url='/login/')
def dashboard(request):
    return HttpResponse("Logged In successfully.")