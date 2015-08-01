
from home.models import Product, CartItem

from django.shortcuts import get_object_or_404 
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.core.mail import send_mail

import random 

CART_ID_SESSION_KEY = 'cart_id' 

# get the current user's cart id, sets new one if blank 
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id() 
    
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = '' 
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890' 

    cart_id_length = 50 
    for y in range(cart_id_length): 
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

# return all items from the current user's cart 
def get_cart_items(request): 
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request):

    # if request.is_ajax():
    #     print ("this is an AJAX Calling")

    print ("start calling add_to_cart method")

    getdata = request.GET.copy()
    
    product_id = getdata.get('product_id','') 
    
    # get quantity added, return 1 if empty 
    quantity = getdata.get('quantity',1)

    p = Product.objects.get(product_id = product_id)

    #get cartitems in cart 
    cart_items = get_cart_items(request) 

    product_in_cart = False
    
    # check to see if item is already in cart 
    for cart_item in cart_items:
        if cart_item.product.product_id == product_id:

            print("Cart item is existed!")

            # update the quantity if found 
            cart_item.add_quantity(quantity)
            product_in_cart = True 
    
    if not product_in_cart:
        # create and save a new cart item 

        print("New Cart item is added!")
        ci = CartItem()
        ci.product = p 
        ci.quantity = quantity 
        ci.cart_id = _cart_id(request)
        ci.save()

    total_products = 0
    for cart_item in cart_items:
        total_products += cart_item.quantity

    #add to test - delete later 
    # context = {'total_products' : total_products}

    # catagory = p.catagory
    # hint_products = Product.objects.filter(catagory = catagory).exclude(product_id = product_id)
    # print(hint_products)
    # return redirect (hint_products)

    context = {}
    print("total products issssssssss", total_products)
    
    # html = render_to_string('home.html')
    # return HttpResponse(html)

    template = "navbar.html"
    return render (request, template, context)

# returns the total number of items in the user's cart 
def cart_distinct_item_count(request): 
    return get_cart_items(request).count()


# return a list of items in a session to cart.html
def go_to_cart(request):

    #get all cartitems in cart 
    cart_items = get_cart_items(request)

    total_products = 0
    total_price = 0
    # get total number of products in cart and total price in cart
    for cart_item in cart_items:
        total_products += cart_item.quantity
        total_price += cart_item.product.price * cart_item.quantity

    context ={'cart_items': cart_items, 'total_products': total_products, 'total_price': total_price}
    template = "cart.html"
    return render (request, template, context)

def send_email (request):

    postdata = request.POST.copy()

    email = postdata.get('email','')
    name = postdata.get('name','')
    address = postdata.get('address','')
    total_products = postdata.get('total_products','')
    total_price = postdata.get('total_price','')

    # Title of email
    title = "Email confirmation content"

    # content of email
    content = "Dear " + name + ", \n \n"
    content += "Thanks for buying at our Demo shop! \n \n Number of products are: "
    content += total_products + " \n \n Your payment is: "
    content += total_price + "€ \n \n The items will be sent to the following address: " 
    content += address + "\n \n Best Regards, \n --------------------------------------- \n Demo shopping cart"

    admin_email = 'demoshopping2015@gmail.com'
    # Send confirmation email to customer
    send_mail (title, content, admin_email, [email])

    #get all cartitems in cart 
    cart_items = get_cart_items(request)

    context = {'email': email, 'name': name, 'address': address,'total_products': total_products, 'total_price': total_price, 'cart_items': cart_items}
    template = "confirmation.html"
    return render (request, template, context)