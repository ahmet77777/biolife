from django.shortcuts import render,redirect,HttpResponseRedirect
from a_panel.forms import *
from home.models import *
from home.forms import LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.models import User

def index(request):

    sub = Subcategory.objects.all()
    cat = Category.objects.all()
    pro = Product.objects.all()
    user = User.objects.filter(is_superuser=False)
    worker = User.objects.filter(is_superuser=True)
    order = Order.objects.filter(status=False)
    order_2 = Order.objects.all()
    customer = Customer.objects.all()
    context = {
        'sub':sub,
        'cat':cat,
        'pro':pro,
        'users':user,
        'workers':worker,
        'orders':order,
        'order_2':order_2,
        'customer':customer,
    }
    return render(request,'a_panel/index.html',context)



        # Category


def category_add(request):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        form = CategoryForm()
        context = {
            'form':form
        }
        return render(request,'a_panel/category/category_add.html',context)
    else:
        return redirect('/a_panel/')

def category_save(request):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        CategoryForm(request.POST).save()
        return redirect("category_all")
    else:
        return redirect('/a_panel/')

def category_all(request):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        all_category = Category.objects.all()
        context = {
            'all_category':all_category,
        }
        return render(request,"a_panel/category/category_all.html",context)
    else:
        return redirect('/a_panel/')

def category_delete(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        Category.objects.get(id=i).delete()
        return redirect('category_all')
    else:
        return redirect('/a_panel/')


def category_edit(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        select_c = Category.objects.get(id=i)
        form = CategoryForm(instance=select_c)
        if request.method == "POST":
            CategoryForm(request.POST,instance=select_c).save()
            return redirect('category_all')
        context = {
            'form':form,
            'select_c':select_c
        }
        return render(request,"a_panel/category/category.edit.html",context)
    else:
        return redirect('/a_panel/')




        # Subcategory



def subcategory_add(request):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        if request.method == "POST":
            SubcategoryForm(request.POST).save()
            return redirect('subcategory_all')
        form = SubcategoryForm()
        context = {
            'form':form
        }
        return render(request,"a_panel/subcategory/subcategory_add.html",context)
    else:
        return redirect('/a_panel/')

def subcategory_all(request):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        all_sub = Subcategory.objects.all()
        context = {
            'all_sub':all_sub,
        }
        return render(request,"a_panel/subcategory/subcategory_all.html",context)
    else:
        return redirect('/a_panel/')

def subcategory_edit(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        select_sub = Subcategory.objects.get(id=i)
        form = SubcategoryForm(instance=select_sub)
        if request.method == "POST":
            SubcategoryForm(request.POST,instance=select_sub).save()
            return redirect('subcategory_all')
        context = {
            'form':form,
        }
        return render(request,"a_panel/subcategory/subcategory.edit.html",context)
    else:
        return redirect('/a_panel/')

def subcategory_delete(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        Subcategory.objects.get(id=i).delete()
        return redirect('subcategory_all')
    else:
        return redirect('/a_panel/')

def subcategory_pro(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        select_sub = Subcategory.objects.get(id=i)
        return render(request,'a_panel/subcategory/subcategory_pro.html',{'select_sub':select_sub})
    else:
        return redirect('/a_panel/')


        #Product


def product_add(request):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        if request.method == "POST":
            ProductForm(request.POST,request.FILES).save()
            return redirect('product_all')
        form = ProductForm()
        context = {
            'form':form
        }
        return render(request,'a_panel/product/product_add.html',context)
    else:
        return redirect('/a_panel/')

def product_all(request):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        all_pro = Product.objects.all()
        context = {
            'all_pro':all_pro
        }
        return render(request,"a_panel/product/product_all.html",context)
    else:
        return redirect('/a_panel/')

def product_detail(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        select_pro = Product.objects.get(id=i)

        context = {
            'select_pro':select_pro,
        }
        return render(request,"a_panel/product/product_detail.html",context)
    else:
        return redirect('/a_panel/')

def product_edit(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        select_pro = Product.objects.get(id=i)
        form = ProductForm(instance=select_pro)
        if request.method == 'POST':
            ProductForm(request.POST,request.FILES,instance=select_pro).save()
            return redirect('product_all')
        return render(request,'a_panel/product/product_edit.html',{'form':form})
    else:
        return redirect('/a_panel/')

def product_delete(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 2:
        Product.objects.get(id=i).delete()
        return redirect('product_all')
    else:
        return redirect('/a_panel/')
        
        # Order
def order(request):
    if request.user.worker.role == 1 or request.user.worker.role == 3:
        all_order = Order.objects.all().exclude(status_2=1)
        return render(request,"a_panel/order/order.html",{"all_order":all_order})
    else:
        return redirect('/a_panel/')
        
def order_detail(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 3:
        order = Order.objects.get(id=i)
        return render(request,"a_panel/order/order_detail.html",{'form':order})
    else:
        return redirect('/a_panel/')
    
def order_delete(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 3:
        order = Order.objects.get(id=i)
        order.status_2 = 1
        order.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/a_panel/')   
def order_remote(request):
    if request.user.worker.role == 1 or request.user.worker.role == 3:
        all_order = Order.objects.filter(status_2=1)
        return render(request,"a_panel/order/order_remote.html",{'all_order':all_order})  
    else:
        return redirect('/a_panel/')  

def order_restore(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 3:
        order = Order.objects.get(id=i)
        order.status_2 = 0
        order.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER","/"))
    else:
        return redirect('/a_panel/')

def order_or(request,i):
    if request.user.worker.role == 1 or request.user.worker.role == 3:
        order = Order.objects.get(id=i)
        if order.status == False:
            order.status = True
        else:
            order.status = False
        order.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER","/"))
    else:
        return redirect('/a_panel/')
    # User

def user_add(request):
    if request.user.worker.role == 1:
    
        if request.method == "POST":
            username = request.POST['username']
            if User.objects.filter(username=username):
                messages.error(request,"Username is")
            form = UserCreateForm(request.POST)
            if form.is_valid():
                password = request.POST['password1']
                user = form.save()
                UserPassword.objects.create(password = password,user=user)
                user.is_superuser = True
                user.save()
                return redirect('user_all')
        form = UserCreateForm()
        return render(request,'a_panel/user/user_add.html',{'form':form})
    else:
        return redirect('/a_panel/')

def user_all(request):
    if request.user.worker.role == 1:
        users = User.objects.filter(is_superuser=True)
        return render(request,'a_panel/user/user_all.html',{'user_all':users})
    else:
        return redirect('/a_panel/')

def user_delete(request,i):
    if request.user.worker.role == 1:

        user = User.objects.get(id=i)
        if not user.username == "admin":
            user.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        return redirect('/a_panel/')
    
def worker_add(request):
    if request.user.worker.role == 1:
        if request.method == "POST":
            form = WorkerForm(request.POST,request.FILES)
            form_2 = form.save()
            return redirect('worker_all')

        form_2 = WorkerForm()
        return render(request,"a_panel/worker/worker_add.html",{'form':form_2})
    else:
        return redirect('/a_panel/')

def worker_all(request):
    if request.user.worker.role == 1:
        all_worker = Worker.objects.all()
        return render(request,'a_panel/worker/worker_all.html',{'all_worker':all_worker})
    else:
        return redirect('/a_panel/')
        
def worker_edit(request,i):
    if request.user.worker.role == 1:
        worker = Worker.objects.get(id=i)
        if request.method == "POST":
            form_w = WorkerForm(request.POST,request.FILES,instance=worker)
            if form_w.is_valid():
                form_w.save()
                return redirect('worker_all')
        form = WorkerForm(instance=worker)
        return render(request,"a_panel/worker/worker_edit.html",{'form':form})
    else:
        return redirect('/a_panel/')
    
def worker_delete(request,i):
    if request.user.worker.role == 1:
        Worker.objects.get(id=i).delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER","/"))
    else:
        return redirect('/a_panel/')

def auth_login(request):
    if request.method == "POST":
        form = UserLoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/a_panel/')
    form = UserLoginForm()
    return render(request,'a_panel/auth_login/auth_login.html',{'form':form})

def auth_logout(request):
    logout(request)
    return redirect('auth_login')

def change_password(request,i):
    if request.user.worker.role == 1:
        user = User.objects.get(id=i)
        if request.method == "POST":
            new_pass = request.POST['password_1']
            user.set_password(new_pass)
            user.save()
            user_pass = user.passwords
            user_pass.password = new_pass
            user_pass.save()
            return redirect('user_all')
        user_pass_2 = user.passwords
        return render(request,"a_panel/user/user_change.html",{"pas":user_pass_2})
    else:
        return redirect('/a_panel/')

def customer_all(request):
    if request.user.worker.role == 1 or request.user.worker.role == 3:

        all_cus = Customer.objects.all()
        return render(request,"a_panel/customer_all.html",{'all_cus':all_cus})
    else:
        return redirect('/a_panel/')

def client_all(request):
    if request.user.worker.role == 1:
        all_client = User.objects.filter(is_superuser=False)
        return render(request,"a_panel/client_all.html",{'all_client':all_client})
    else:
        return redirect('/a_panel/')
    
def client_delete(request,i):
    if request.user.worker.role == 1:
        User.objects.get(id=i).delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER","/"))
    else:
        return redirect('/a_panel/')
# Create your views here.
