from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    
class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural = "Course Categories"
    
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    address = models.TextField()
    interested_categories = models.TextField()
    

    
