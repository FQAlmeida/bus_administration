from django.db import models

class Bus(models.Model):
    serial = models.CharField(max_length=50, unique=True)
    lotacao = models.IntegerField()

    def __str__(self):
        return f"Serial: {self.serial}\nLotação: {self.lotacao}"