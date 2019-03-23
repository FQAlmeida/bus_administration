from django.db import models

class Passager(models.Model):
    name = models.CharField(max_length=150)
    document = models.CharField(max_length=11)

    def __str__(self):
        return f"Name: {self.name}\nDocument: {self.document}"