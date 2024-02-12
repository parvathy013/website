from django.urls import path
from.import views
app_name='companyapp'

urlpatterns = [
  
    path('',views.login, name='login'),
    path('studash',views.studash, name='studash'),
    path('clidash',views.clidash, name='clidash'),
    path('student/',views.student, name='student'),
]