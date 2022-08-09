from statistics import mode
from tkinter import CASCADE
from django.db import models

class Student(models.Model):
    register_num=models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')
    place = models.CharField(max_length=100, blank=True, default='')
    admn_year=models.IntegerField()
    
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    register_num=models.IntegerField()
    english = models.CharField(max_length=100, blank=True, default='')
    maths = models.CharField(max_length=100, blank=True, default='')
    physics = models.CharField(max_length=100, blank=True, default='')
    cs = models.CharField(max_length=100, blank=True, default='')
    chemistry = models.CharField(max_length=100, blank=True, default='')
    
     
    