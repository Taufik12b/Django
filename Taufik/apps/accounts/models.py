from django.db import models

# Create your models here.

class Student(models.Model):

    BRANCH_CHOICES = {
        "CS" : "Computer Science",
        "AI" : "Artificial Intelligence",
        "DS" : "Data Science"
    }
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(max_length=250)
    age = models.IntegerField()
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.branch}"
