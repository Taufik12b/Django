from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Student

# Create your views here.

def home(request):
    return render(request,"accounts.html")
    # return HttpResponse("This is accounts app")

def login(request):
    return HttpResponse("Login Page")

def students(request):
    students = Student.objects.all()
    return render(request,'student_list.html',{"students":students})

def add_student(request):
    if request.method=="POST":
        name = request.POST["name"]
        image = request.FILES.get("image") 
        email = request.POST.get("email")
        age = request.POST.get("age")
        branch = request.POST.get("branch")

        student = Student(
            name = name,
            image = image,
            email = email,
            age = age,
            branch = branch,
        )
        student.save()
        return redirect("students")
    return render(request,"add_student.html")

def update_student(request, id):
    student = Student.objects.filter(id=id).first()
    if request.method=="POST":
        name = request.POST["name"]
        image = request.FILES.get("image") 
        email = request.POST.get("email")
        age = request.POST.get("age")
        branch = request.POST.get("branch")
        student.name = name
        student.age = age
        student.email = email
        student.branch = branch
        if image:
            student.image = image
        student.save()
        return redirect("students")
    return render(request,"update_student.html",{"student":student})

def delete_student(request, id):
    student = Student.objects.filter(id=id).first()
    student.delete()
    return redirect("students")
