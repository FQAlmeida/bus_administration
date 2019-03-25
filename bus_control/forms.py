from django.forms import ModelForm
from django.forms import DateTimeField
from django.utils.dateparse import datetime 
from djmoney.forms import MoneyWidget

from .models import Trade, Passage

class TradeForm(ModelForm):
    date = DateTimeField(initial=datetime.datetime.now())
    class Meta:
        model = Trade
        fields = "__all__"