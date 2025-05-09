from django.core.mail import send_mail
from django.conf import settings

# Sending Test email 
def sendTestEmail(email, subject, message):
    # subject, message, from_email = settings.EMAIL_HOST_USER, receipent email 
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

# Call above function in shell


# Send otp to email
def sendOTPToEmail(email, subject, message):
    # subject, message, from_email = settings.EMAIL_HOST_USER, receipent email 
    # send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
    print("EMAIL SENT!")