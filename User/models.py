from django.db import models
from Book.models import Book

class Registration(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Email=models.EmailField(primary_key=True)
    Contact_no=models.IntegerField(unique=True)
    Password=models.CharField(max_length=50)
    #Books=models.ForeignKey(Book,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.First_name+" "+self.Last_name
    
class UserQuery(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    query_desc = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    