from django.urls import path
from.import views
app_name='mainapp'

urlpatterns = [
  
    path('',views.master, name='master'),
    path('service',views.service, name='service'),
    path('contact',views.contact, name='contact'),
    path('register',views.register,name='register'),
    path('careers', views.careers, name='careers'),
    path('client', views.client, name='client'),
]
