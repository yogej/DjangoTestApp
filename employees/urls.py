
from django.urls import path
from . import views


urlpatterns =[
    path('add/', views.add_employee,name='add_members'),
    path('view/', views.getEmployees,name='show_employee'),

    
]