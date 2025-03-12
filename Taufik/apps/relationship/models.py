from django.db import models

# Create your models here.


# one to one relationship

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.IntegerField()


# many to one relationship

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# many to any relationship
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    course = models.ManyToManyField(Course)
    
    def __str__(self):
        return self.name