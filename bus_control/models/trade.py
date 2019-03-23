from django.db import models
from djmoney.models.fields import MoneyField
from . import (Passage)

class Trade(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    total = MoneyField(max_digits=19, decimal_places=2, default_currency="BRL")
    passages = models.ManyToManyField(Passage)

    