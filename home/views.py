from venv import logger
from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from a_panel.models import *
from home.forms import *
from home.models import *
from django.db.models.functions import Lower
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import logging
 


logger = logging.getLogger(__name__)

def index(request):
    return render(request,"home/index.html")

filter_number = [
    {'val':'1','text':'Under $25','id':'1'},
    {'val':'2','text':'$25 to $50','id':'2'},
    {'val':'3','text':'$50 to $100','id':'3'},
    {'val':'4','text':'$200 & Above','id':'4'},
]

filter_number_2 = [
    {'val':'0','text':'Price','id':'1'},
    {'val':'1','text':'Under $25','id':'1'},
    {'val':'2','text':'$25 to $50','id':'2'},
    {'val':'3','text':'$50 to $100','id':'3'},
    {'val':'4','text':'$200 & Above','id':'4'},
]

filter_name = [
    {'val':'sort','text':'---'},
    {'val':'AZ','text':'A-Z'},
    {'val':'ZA','text':'Z-A'},
    {'val':'-1','text':'price: low to high'},
    {'val':'-0','text':'price: high to low'},
]

def category(request, i):
    select_subcategory = Subcategory.objects.get(id=i)
    select_pro = Product.objects.filter(subcategory=select_subcategory)
    sub = Subcategory.objects.exclude(id=i)[:5]

    filter_price = request.GET.get("filter-price")
    filter_sort = request.GET.get('filter-sort')

    filter_conditions = {
        '0': {'price_new__gte': 0},
        '1': {'price_new__lte': 25},
        '2': {'price_new__lte': 50, 'price_new__gt': 25},
        '3': {'price_new__lte': 100, 'price_new__gt': 50},
        '4': {'price_new__gte': 200}
    }
    if filter_price in filter_conditions:
        select_pro = select_pro.filter(**filter_conditions[filter_price])

    sort_methods = {
        'AZ': Lower('name'),
        'ZA': Lower('name').desc(),
        '-1': 'price_new',
        '-0': '-price_new'
    }
    if filter_sort in sort_methods:
        select_pro = select_pro.order_by(sort_methods[filter_sort])

    paginator = Paginator(select_pro, 4)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        products = paginator.page(1)

    if request.method == "POST":
        num_1 = request.POST['price-from']
        num_2 = request.POST['price-from_2']
     
        sub_filter = Product.objects.filter(subcategory=select_subcategory,price_new__gt = num_1,price_new__lt=num_2)
        context = {
            'num_1':num_1,
            'num_2':num_2,
            'products':sub_filter,
            'sub':sub,
            'filter_number':filter_number,
            'filter_price':filter_price,
            'filter_price_2':filter_number_2,
            'filter_name':filter_name,
            'sub_2':select_subcategory,
            'filter_sort':filter_sort,
            'page':page_number,

    }
        
        return render(request,"home/category.html",context)
    
    context = {
        'sub_2':select_subcategory,
        'products': products,
        'sub': sub,
        'filter_price': filter_price,
        'filter_price_2':filter_number,
        'filter_sort': filter_sort,
        'page_number': page_number,
        'filter_name':filter_name,
    }

    return render(request, "home/category.html", context)


def category_left(request,i):
    select_subcategory = Subcategory.objects.get(id=i)
    select_pro = Product.objects.filter(subcategory=select_subcategory)
    sub = Subcategory.objects.exclude(id=i)[:5]

    filter_price = request.GET.get("filter-price")
    filter_sort = request.GET.get('filter-sort')

    filter_conditions = {
        '0': {'price_new__gte': 0},
        '1': {'price_new__lte': 25},
        '2': {'price_new__lte': 50, 'price_new__gt': 25},
        '3': {'price_new__lte': 100, 'price_new__gt': 50},
        '4': {'price_new__gte': 200}
    }
    if filter_price in filter_conditions:
        select_pro = select_pro.filter(**filter_conditions[filter_price])

    sort_methods = {
        'AZ': Lower('name'),
        'ZA': Lower('name').desc(),
        '-1': 'price_new',
        '-0': '-price_new'
    }
    if filter_sort in sort_methods:
        select_pro = select_pro.order_by(sort_methods[filter_sort])

    paginator = Paginator(select_pro, 4)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        products = paginator.page(1)

    if request.method == "POST":
        num_1 = request.POST['price-from']
        num_2 = request.POST['price-from_2']
     
        sub_filter = Product.objects.filter(subcategory=select_subcategory,price_new__gt = num_1,price_new__lt=num_2)
        context = {
            'num_1':num_1,
            'num_2':num_2,
            'products':sub_filter,
            'sub':sub,
            'filter_number':filter_number,
            'filter_price':filter_price,
            'filter_price_2':filter_number_2,
            'filter_name':filter_name,
            'sub_2':select_subcategory,
            'filter_sort':filter_sort,
            'page':page_number,

    }
        
        return render(request,"home/category.html",context)
    
    context_2 = {
        'sub_2':select_subcategory,
        'products': products,
        'sub': sub,
        'filter_price': filter_price,
        'filter_price_2':filter_number,
        'filter_sort': filter_sort,
        'page_number': page_number,
        'filter_name':filter_name,
    }

    return render(request,"home/category_left.html",context_2)

def random_generator(number):
    password = ''
    for i in range(number):
        step = random.randint(1,3)
        if step == 1:
            password += str(random.randint(1,9))
        if step == 2:
            password += chr(random.randint(65,90))
    return password







def send_message_to_customer(user, pincode):
    try:
        subject = 'Registration Confirmation'
        message = f'Hi {user.username}, your pincode for activation is {pincode}.'
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]
        send_mail(subject, message, from_email, to_email)
        logger.info('Confirmation message sent to %s', user.email)
        return True
    except Exception as e:
        logger.error('Failed to send confirmation message to %s: %s', user.email, str(e))
        return False


def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            pincode = random_generator(6)
            login(request, user)
            Activ.objects.get_or_create(user=user, pincode=pincode)
            if not send_message_to_customer(user, pincode):
                messages.error(request, 'Failed to send confirmation message')
            else:
                logger.info('User registered successfully: %s', user.username)
                return redirect('active')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = RegisterForm()
    
    return render(request, "home/register.html", {'form': form})


def logn(request):
    if request.method == "POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
    form = LoginForm()
    return render(request,'home/login.html',{'form':form})


def active(request):
    if request.method == "POST":
        active_code = request.POST.get('active', None)
        if active_code:
            
            if request.user.is_authenticated:
                
                user_activ = get_object_or_404(Activ, user=request.user)
       
                if user_activ.pincode == active_code:

                    user_activ.status = True
                    user_activ.save()
                    messages.success(request, 'Your account has been activated successfully!')
                    return redirect('/')
                else:
                    messages.error(request, 'Incorrect activation code.')
            else:
                messages.error(request, 'Please log in to activate your account.')
        else:
            messages.error(request, 'Please provide an activation code.')
    return render(request, "home/active.html")




def log(request):
    if request.user.is_authenticated:
        if request.user.activecode.status == False:
            User.objects.filter(username=request.user.username).delete()
            return redirect('/')
        else:
            logout(request)
    return redirect('/')
    
def product(request,i):
    pro = Product.objects.get(id=i)
    cart = CartItem.objects.filter(product=pro)
    context = {
        'product':pro,
        'cartitem':cart
    }
    return render(request,"home/product.html",context)


def addprocart(request, i):
    if request.user.is_authenticated:
        try:
            product = Product.objects.get(id=i)
        except Product.DoesNotExist:
            return redirect('/')

        cart, created = Cart.objects.get_or_create(user=request.user, status=False)
        cartitem, created = CartItem.objects.get_or_create(product=product, cart=cart)
        cartitem.quatity += 1
        cartitem.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return redirect('login') 
    
def addprocart_2(request):
 
    product_id = request.POST.get('product_id')
    cart,created = Cart.objects.get_or_create(user=request.user,status= False)
    cartitem,created = CartItem.objects.get_or_create(product=product_id,cart=cart)
    cartitem.quatity += 1
    cartitem.save()
    print(request.POST.get('quantity_'))
    return JsonResponse({},status=200)


def procartdel(request,i):
    if request.user.is_authenticated:
        product = Product.objects.get(id=i)
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
        cartitem,created = CartItem.objects.get_or_create(product=product,cart=cart)
        cartitem.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('logn')

def product_delete(request,i):
    if request.user.is_authenticated:
        product = Product.objects.get(id=i)
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
        cartitem,created = CartItem.objects.get_or_create(product=product,cart=cart)
        if cartitem.quatity > 0:
            cartitem.quatity -= 1
        cartitem.save()
        if cartitem.quatity == 0:
            cartitem.delete()
    
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('logn')


def shopping(request):
    return render(request,"home/shopping.html")


def checkout(request):
    if request.user.is_authenticated:
        form = OrderForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                order = form.save(commit=False)
                cart = request.user.carts.filter(status=False).first()
                if cart:
                    order.cart = cart
                    cart.status = True
                    cart.save()
                    order.save()
                    return redirect('/')  
                else:
                    return render(request, "home/checkout.html", {'form': form, 'error_message': 'No active cart found.'})
        return render(request, "home/checkout.html", {'form': form})
    else:
        return redirect('logт')



def search_sub(request):
    src = request.GET.get('search')
    sub = request.GET.get('subcategory')
    d = "="

    pro = Product.objects.filter(name__icontains=src)
    if sub != '-1':
        try:
            subc = Subcategory.objects.get(id=sub)
            pro = pro.filter(subcategory=subc)
        except Subcategory.DoesNotExist:
            pass

    filter_price = request.GET.get("filter-price")
    filter_sort = request.GET.get("filter-sort")

    # Фильтрация по цене
    price_filters = {
        '0': {'price_new__gte': 0},
        '1': {'price_new__lte': 25},
        '2': {'price_new__lte': 50, 'price_new__gte': 25},
        '3': {'price_new__gte': 50, 'price_new__lte': 100},
        '4': {'price_new__gte': 200}
    }
    if filter_price in price_filters:
        pro = pro.filter(**price_filters[filter_price])

    # Сортировка
    sort_methods = {
        'AZ': Lower('name'),
        'ZA': Lower('name').desc(),
        '-1': '-price_new',
        '-0': 'price_new'
    }
    if filter_sort in sort_methods:
        pro = pro.order_by(sort_methods[filter_sort])

    paginator = Paginator(pro, 2)
    page_number = request.GET.get('page')

    try:
        prod = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        prod = paginator.page(1)

    context = {
        'pro': prod,
        'src': src,
        'sub': sub,
        'filter_price': filter_price,
        'filter_sort': filter_sort,
        'page_number': page_number,
        'filter_price_2':filter_number,
        'filter_name': filter_name,
    }

    return render(request, 'home/search.html', context)


def wishlist_add(request,i):
    if request.user.is_authenticated:
        product =  Product.objects.get(id=i)
        wishlist,created = Wishlist.objects.get_or_create(user=request.user)
        wishitems ,created = WishlistItems.objects.get_or_create(product=product,wishlist=wishlist)
        wishitems.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('logn')
    
def wishlist_delete(request,i):
    if request.user.is_authenticated:

        pro = Product.objects.get(id=i)
        wishlist,created = Wishlist.objects.get_or_create(user=request.user)
        wishitems ,created = WishlistItems.objects.get_or_create(product=pro,wishlist=wishlist)

        wishitems.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
            return redirect('logn')

def wishlist(request):
    if request.user.is_authenticated:
        wish = Wishlist.objects.filter(user=request.user)
        return render(request,'home/wishlist.html',{'wishlist':wish})
    else:
        return render(request,'home/wishlist.html')


def contact(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    con = CustomerForm()
    return render(request,'home/contact.html',{'form':con})


# Create your views here.
