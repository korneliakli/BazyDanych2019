from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_order, name="make-order"),
    path('add_order_details/?id=<id>/', views.add_order_details,name="order-details"),
    path('show_orders/', views.OrderList.as_view(), name="show-orders"),
]