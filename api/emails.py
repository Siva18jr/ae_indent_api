from django.core.mail import send_mail
from django.conf import settings

def sendOtpViaEmail(email, otp):
    
    subject = 'AE Indent account verification email'
    message = f'Your otp is {otp}'
    emailFrom = settings.EMAIL_HOST
    
    send_mail(subject, message, emailFrom, [email])