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
    date = datetime.datetime()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.category.name} - {self.date}"

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} - {self.category.name} - {self.date}"    