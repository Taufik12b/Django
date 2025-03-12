from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {"title":"Django", 
                                          "user_name":"Taufik Ansari",
                                          "languages":["C++","HTML","Python"],
                                          "logedIn":True})
    # return HttpResponse("This is Home page")

def about(request):
    return HttpResponse("This is about page")