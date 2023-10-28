from django.urls import path
from .views import StoreView, CartView, CheckOutView



urlpatterns = [
    path("", StoreView.as_view(), name="store"),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckOutView.as_view(), name="checkout"),
]