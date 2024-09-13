# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_welcome_email
from myapp.models import Signup


def signup_view(request):
    # Your logic for handling user signup
    if request.method == "POST":
        name = request.POST.get("name")
        email_address = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        signup, created = Signup.objects.get_or_create(
            email=email_address, defaults={"name": name, "phone_number": phone_number}
        )
        send_welcome_email.delay(email_address)
        return HttpResponse("Signup successful!")
    return render(request, "signup.html")
