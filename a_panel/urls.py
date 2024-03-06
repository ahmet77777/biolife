
from django.urls import path,include
from a_panel import views

urlpatterns = [
    path('',views.index),
    path('category_add/',views.category_add,name='category_add'),
    path('category_save/',views.category_save,name='category_save'),
    path('category_all/',views.category_all,name='category_all'),
    path('category_delete/',views.category_delete,name='category_delete'),
    path('category_edit/<int:i>',views.category_edit,name='category_edit'),

    # Subcategory

    path('subcategory_add/',views.subcategory_add,name='subcategory_add'),
    path('subcategory_all/',views.subcategory_all,name='subcategory_all'),
    path('subcategory_delete/',views.subcategory_delete,name='subcategory_delete'),
    path('subcategory_edit/<int:i>',views.subcategory_edit,name='subcategory_edit'),
    path('subcategory_pro/<int:i>',views.subcategory_pro,name='subcategory_pro'),

    # Product

    path('product_add/',views.product_add,name='product_add'),
    path('product_all/',views.product_all,name='product_all'),
    path('product_detail/<int:i>',views.product_detail,name='product_detail'),
    path('product_edit/<int:i>',views.product_edit,name='product_edit'),
    path('product_delete/',views.product_delete,name='product_delete'),

    # Order

    path('order/',views.order,name='order'),
    path('order_detail/<int:i>',views.order_detail,name='order_detail'),
    path('order_delete/<int:i>',views.order_delete,name='order_delete'),
    path('order_remote/',views.order_remote,name='order_remote'),
    path('order_restore/<int:i>',views.order_restore,name='order_restore'),
    path('order_or/<int:i>',views.order_or,name='order_or'),
    
    # User

    path('user_add/',views.user_add,name='user_add'),
    path('user_all/',views.user_all,name='user_all'),
    path('change_password/<int:i>',views.change_password,name='change_password'),
    path('user_delete/<int:i>',views.user_delete,name='user_delete'),

    # Worker
    path('worker_add/',views.worker_add,name='worker_add'),
    path('worker_all/',views.worker_all,name='worker_all'),
    path('worker_edit/<int:i>',views.worker_edit,name='worker_edit'),
    path('worker_delete/<int:i>',views.worker_delete,name='worker_delete'),

    # Login

    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_logout/',views.auth_logout,name='auth_logout'),
    # path('change_pass',)

    # Contact

    path('customer_all/',views.customer_all,name='customer_all'),
    path('client_all/',views.client_all,name='client_all'),
    path('client_delete/<int:i>',views.client_delete,name='client_delete'),


]
