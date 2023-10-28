from django.shortcuts import render
from django.views import View

from store.models import Product


class StoreView(View):
    def get(self, request):
        product = Product.objects.all()
        context = {
            'product': product
        }
        return render(request,"store.html", context)



class CartView(View):
    def get(self, request):
        context = {

        }
        return render(request, "cart.html", context)



class CheckOutView(View):
    def get(self, request):
        context = {

        }
        return render(request, "checkout.html", context)





