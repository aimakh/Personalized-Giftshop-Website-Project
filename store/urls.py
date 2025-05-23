from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('signup/', views.signup, name='signup'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),  
    path('remove-from-cart/<int:index>/', views.remove_from_cart, name='remove_from_cart'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('checkout/', views.create_order, name='checkout'),
    path('migrate_cart/', views.migrate_guest_cart_to_user, name='migrate_cart'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
]