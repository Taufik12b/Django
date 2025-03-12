from django.shortcuts import render, redirect

from .forms import ContactForm

# Create your views here.

def home(request):
    if request.method=="POST":
        form  = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # print(name, email)
            form.save()
            return redirect("students")
    form = ContactForm()
    return render(request, "contact.html", {"form": form})
