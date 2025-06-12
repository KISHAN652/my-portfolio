from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to MongoDB via Django model
        Contact(name=name, email=email, subject=subject, message=message).save()

        # Send email to your Gmail
        send_mail(
            f"New Contact Message: {subject}",
            f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            settings.DEFAULT_FROM_EMAIL,  # use your Gmail from settings
            ['gajjarsk111@gmail.com'],    # your email to receive messages
            fail_silently=False,
        )

        return render(request,'thank_you.html')

    return HttpResponse("❌ Invalid request")
# This code defines the views for the contactme app.
# It includes an index view to render the home page and a submit_form view to handle form submissions.