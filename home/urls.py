from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index),
    path('category/<int:i>',views.category,name='category'),
    path('category_left/<int:i>',views.category_left,name='category_left'),
    path('reg/',views.reg,name='reg'),
    path('active/',views.active,name='active'),
    path('log/',views.log,name='log'),
    path('product/<int:i>',views.product,name='product'),
    path('addprocart/<int:i>',views.addprocart,name='addprocart'),
    path('addprocart_2/',views.addprocart_2,name='addprocart_2'),
    path('logn/',views.logn,name='logn'),
    path('procartdel/<int:i>',views.procartdel,name='procartdel'),
    path('product_delete/<int:i>',views.product_delete,name='product_delete'),
    path('shopping/',views.shopping,name='shopping'),
    path('checkout/',views.checkout,name='checkout'),
    path('search_sub/',views.search_sub,name='search_sub'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('wishlist_add/<int:i>',views.wishlist_add,name='wishlist_add'), 
    path('contact/',views.contact,name='contact'),
    path('wishlist_delete/<int:i>',views.wishlist_delete,name='wishlist_delete'),

]
