from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User 
from django.core.mail import send_mail
from django.http import HttpResponse

@receiver(post_save,sender = User)
def send_welcome_email(sender ,  instance , created , **kwargs):
    if created:
        print("New User is:", {instance.username})
        subject = "Welcome to My Notes making App"
        message = f"Hi {instance.username} , Thankyou for Registering ."
        from_email = 'dangerm249@gmail.com'
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        print("📧 Welcome email sent to:", instance.email)
