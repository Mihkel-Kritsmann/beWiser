from django.db import models

# Create your models here.
class Expense(models.Model):
    title = models.CharField('expense_text' ,max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    CATEGORY = [
        ('UNKOWN', 'unknown',
        'FOOD', 'food',
        'RENT', 'rent',
        'OTHER', 'other')
    ]
    def __str__(self):
        return self.title
