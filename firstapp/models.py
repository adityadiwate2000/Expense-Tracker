from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title
