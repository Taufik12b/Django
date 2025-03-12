from django.shortcuts import render, redirect
from .models import MediaFiles

# Create your views here.

def upload(request):
    if request.method=="POST":
        file_name = request.POST["file_name"]
        upload_file = request.FILES["upload_file"]
        MediaFiles.objects.create(
            file_name = file_name,
            upload_file = upload_file
        )
        return redirect("upload")
    uploads = MediaFiles.objects.all()
    return render(request, "upload.html", {"uploads":uploads})
