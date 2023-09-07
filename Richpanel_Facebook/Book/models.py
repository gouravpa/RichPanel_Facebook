from django.db import models
class Book(models.Model):
    ISBN=models.CharField(max_length=13)
    Book_name=models.CharField(max_length=20)
    Author_name=models.CharField(max_length=20)
    Title=models.CharField(max_length=200)
    def __str__(self):
        return self.Book_name
    
    
    
    
