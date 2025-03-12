from django.contrib import admin

from .models import User, Profile, Category, Product, Course, Student

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Course)
admin.site.register(Student)


