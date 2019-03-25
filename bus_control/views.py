from django.shortcuts import render, redirect, resolve_url
from django.views.generic import View, CreateView

from .models import Passager, Trade

# Create your views here.

class HomeView(View):
    def get(self, request):
        return redirect("bus_control:trades_master")

class PassagerMasterView(View):
    template_name = "bus_control/passager_master.html"
    def get(self, request):
        passagers = Passager.objects.all()
        return render(request, self.template_name, context={"passagers": passagers})

class TradeMasterView(View):
    template_name = "bus_control/trades_master.html"
    def get(self, request):
        trades = Trade.objects.all()
        return render(request, self.template_name, context={"trades": trades})

class TradeAddView(CreateView):
    model = Trade
    fields = [
        "date",
        "passages",
        "total",
    ]
