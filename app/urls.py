
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('add/<int:id>/',views.add_to_cart,name='add'),
    path('update_quantity/', views.update_quantity, name='update_quantity'),
    path('remove/<int:cart_item_id>/',views.remove_from_cart,name='remove'),
]
