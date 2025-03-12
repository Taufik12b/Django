from django.shortcuts import render, redirect

from django.contrib.auth.models import User

# Create your views here.

def home(request):
    users = User.objects.all()
    return render(request, "accounts.html", {"users":users})

def create_user(request):
    # User.objects.create_user(
    #     username="Mike",
    #     password="12345678"
    # )
    user = User.objects.filter(username="Mike").first()
    # user.username = "Tushar Kapoor"
    user.set_password("8527627524")
    user.save()
    return redirect(home)
