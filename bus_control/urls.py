from django.urls import path 

from .views import (PassagerMasterView, TradeMasterView)

app_name = "bus_control"

urlpatterns = [
    path("", PassagerMasterView.as_view() , name = "passagers"),
    path("trades/", TradeMasterView.as_view() , name = "trades"),
]
