from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.


class   Professor(models.Model):
    name= models.CharField(max_length= 200)
    email= models.EmailField()  
    contact_number = models.IntegerField()
    acheivements = models.CharField(max_length = 200)
    stream = models.CharField(max_length=200)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.URLField(max_length=1000)

class Acheivement(models.Model):
    id_of_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    acheivement = models.CharField(max_length=200)

class Student(models.Model):
    name= models.CharField(max_length= 200)
    email= models.EmailField()
    contact_number = models.IntegerField()
    acheivements = models.CharField(max_length = 200)
    stream = models.CharField(max_length=200)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.URLField(max_length=1000)