from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Product,Cart,CartItem
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def index(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'index.html',context)

def register(request):
    return render(request,'register.html')

def cart(request):
    cart_items = CartItem.objects.all()
    total_price = 0
   
# add to cat items

    for cart_item in cart_items: 
        cart_item.total_price = cart_item.product.price * cart_item.quantity
        total_price += cart_item.total_price

    total_carted_items = cart_items.count()
    total_amount = sum(cart_item.total_price for cart_item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_carted_items': total_carted_items,
        'total_amount': total_amount,
    }
    return render(request,'cart.html',context)


def checkout(request):
    cart_items = CartItem.objects.all()

    total_price = 0
   
# total the cart amount

    for cart_item in cart_items:
        cart_item.total_price = cart_item.product.price * cart_item.quantity
        total_price += cart_item.total_price

    total_carted_items = cart_items.count()
    total_amount = sum(cart_item.total_price for cart_item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_carted_items': total_carted_items,
        'total_amount': total_amount,
    }
    return render(request,'checkout.html',context)

# add to the cart

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def update_quantity(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        new_quantity = int(request.POST.get('new_quantity'))

        # Assuming you have a model named CartItem with 'quantity' field.
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity = new_quantity
        cart_item.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
        
# remove cart

def remove_from_cart(request,cart_item_id):
    cart_item=get_object_or_404(CartItem,id=cart_item_id)
    cart_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart_view(request):
    cart_items = CartItem.objects.all()
    cart_count = cart_items.count()

    return render(request, 'base.html', {'cart_items': cart_items, 'cart_count': cart_count})


