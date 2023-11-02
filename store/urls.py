from django.urls import path
from .views import StoreView, CartView, CheckOutView, updateItem, processOrder



urlpatterns = [
    path("", StoreView.as_view(), name="store"),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckOutView.as_view(), name="checkout"),
    path("update-item/", updateItem, name="update-item"),
    path("process-order/", processOrder, name="process-order"),
]