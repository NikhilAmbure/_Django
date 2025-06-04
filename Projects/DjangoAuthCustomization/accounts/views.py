from django.shortcuts import render, redirect
# Here, instead of 'User' we want to import 'Custom user model'
from django.contrib.auth import get_user_model, login
from .emailer import sendOTPToEmail
import random
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.core.cache import cache

# Customized user model
User = get_user_model()

# Sending an email by logging in with phone number (with extended abstractuser which contains his email)
def login_page(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        

        # Rate Limiting
        # If any user attempts the OTP for multiple times then apply rate limiting on it
        # Like after 2 attempts of resending otp , we can give him 5min cooldown for next attempt of otp
        if cache.get(phone_number):
            data = cache.get(phone_number)
            print(data)
            # OTP attempt count 
            data['count'] += 1

            # If count >= 3 -> set rate limiting to 5min for next otp
            if data['count'] >= 3:
                cache.set(phone_number, data, 60 * 5)
                messages.error(request, "You can request OTP after 5min.")
                redirect('/')

            cache.set(phone_number, data, 60 * 1)
        
        if not cache.get(phone_number):
            data = {
                "phone_number": phone_number,
                "count": 1
            }
            cache.set(phone_number, data, 60 * 1)



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
        user_obj = User.objects.get(id = user_id)

        # In case of phishing attacks for multiple requests of otps
        # To protect the routes from hackers
        if cache.get(user_obj.phone_number):
            data = cache.get(user_obj.phone_number)

            if data['count'] >= 3:
                messages.error(request, "You can request OTP after 5min.")
                redirect('/')

        otp = request.POST.get('otp')

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