from django.shortcuts import render
from django.views.generic import View

from .models import Passager, Trade

# Create your views here.

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
