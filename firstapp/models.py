from django.db import models

class Expense(models.Model):
    amount = models.IntegerField()
    category = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"Expense - Amount: {self.amount}, Category: {self.category}, Date: {self.date}"
