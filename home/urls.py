from django.urls import path,include, reverse_lazy
from home import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


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

    path('password-reset/',PasswordResetView.as_view(template_name='home/password_reset_form.html',email_template_name='home/password_reset_email.html',success_url=reverse_lazy('password_reset_done')),name='password_reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='home/password_reset_done.html'),name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='home/password_reset_confirm.html',success_url=reverse_lazy('password_reset_complate')),name='password_reset_confirm'),
    path('password-reset/complate/',PasswordResetCompleteView.as_view(template_name='home/password_reset_complete.html'),name='password_reset_complate')

]
