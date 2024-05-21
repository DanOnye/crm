from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('customer/<int:pk>', views.customer_page, name="customer"),
    path('customer_delete/<int:pk>', views.delete_customer, name="delete"),
    path('customer_add/', views.add_customer, name="add"),
    path('customer_update/<int:pk>', views.update_customer, name="update"),
]
