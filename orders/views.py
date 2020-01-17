from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.forms import formset_factory, inlineformset_factory
from django.views.generic.edit import FormView
from django.db.models import Sum
from northwind.models import Orders as OrdersModel  
from northwind.models import OrderDetails as OrderDetailsModel 
from northwind.models import Products
from .forms import make_order_form, add_products 

def make_order(request):
    order=OrdersModel()
    if request.method == 'POST':
        order_form = make_order_form(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            return redirect('../add_order_details/?id=' + str(order.order_id) + '/')
    else:
        order_form = make_order_form(instance=order)
    return render(request, 'orders/add_order.html', context = {'order_form': order_form,'order': order})

def add_order_details(request):
    order_id = request.GET.get('id', '')
    order_details = OrderDetailsModel
    if request.method == 'POST':
        order_details_form = add_products(request.POST)
        if order_details_form.is_valid():
            order_details = order_details_form.save()
            order_details.order_id = order_id
            prd_id = order_details_form.cleaned_data.get('product_id')
            unit_price = Products.objects.filter(product_id = prd_id).unit_price
            order_details.unit_price = unit_price
            order_details.save()
            return redirect('../add_order_details/?id=' + str(order_id) + '/')
    else:
        order_details_form= add_products(instance=order_details)
    return render(request, 'orders/add_order_details.html', context = {'order_details_form': order_details_form,'order_id': order_id})


class OrderList(generic.ListView):
    template_name = 'orders/show_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return OrdersModel.objects.order_by('order_id')