#1.Create a model representing a company with departments and employees, using ForeignKey relationships
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Employees(models.Model):
    name =models.CharField(max_length=100)

    department = models.ForeignKey(Department, on_delete= models.CASCADE, related_name= 'employees')

#2.Create a model for a product and its detailed description using a OneToOneField
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()

#3.Implement a ManyToManyField to model the relationship between students and courses