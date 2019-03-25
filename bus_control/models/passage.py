
from django.db import models
from djmoney.models.fields import MoneyField
from .passager import (Passager)
from .travel import (Travel)

class Passage(models.Model):
    passager = models.ForeignKey(Passager, verbose_name="Passager", on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, verbose_name="Travel", on_delete=models.CASCADE)
    price = MoneyField(max_digits=19, decimal_places=2, default_currency="BRL")

    def __str__(self):
        return f"{self.passager} {self.price}"
    