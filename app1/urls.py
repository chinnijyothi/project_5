from django.urls import path
from app1 .views import *
app_name='this is my app1 first view'
urlpatterns=[
    path('first/',first,name='first')
]