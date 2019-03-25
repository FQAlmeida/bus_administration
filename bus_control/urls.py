from django.urls import path 

from .views import (PassagerMasterView, TradeMasterView, HomeView, TradeAddView)

app_name = "bus_control"

urlpatterns = [
    path("", HomeView.as_view() , name = "home"),
    path("passager/", PassagerMasterView.as_view(), name= "passagers"),
    path("trades/", TradeMasterView.as_view() , name = "trades_master"),
    path("trades/add", TradeAddView.as_view() , name = "trades_add"),
]
