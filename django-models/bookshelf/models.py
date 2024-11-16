from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100,default='Anonymous')

class Book(models.Model):
    title = models.CharField(max_length=200, default='Anonymous')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='Anonymous')
    publication_year = models.DateField()

    def __str__(self):
        return self.title