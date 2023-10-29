from django.shortcuts import render
from django.views import View

from store.models import Product, Order


class StoreView(View):
    def get(self, request):
        product = Product.objects.all()
        context = {
            'product': product
        }
        return render(request,"store.html", context)



class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
        sum = 0
        for i in items:
            sum+= i.get_total()
        quantity = 0
        for j in items:
            quantity += j.quantity


        context = {
            "quantity": quantity,
            "sum":sum,
            "items": items
        }
        return render(request, "cart.html", context)



class CheckOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
        sum = 0
        for i in items:
            sum += i.get_total()
        quantity = 0
        for j in items:
            quantity += j.quantity

        context = {
            "quantity": quantity,
            "sum": sum,
            "items": items
        }
        return render(request, "checkout.html", context)





