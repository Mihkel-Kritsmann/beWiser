from django.db import models
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField('date of transaction', auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.amount} - {self.category.name}"    

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
<<<<<<< HEAD
    #date = models.DateTimeField('date of transaction', auto_now_add=True)
=======
    date = models.DateTimeField('date of transaction', auto_now_add=True)
>>>>>>> refs/remotes/origin/main
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.amount} - {self.category.name}"    