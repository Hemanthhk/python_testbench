#The idea of this file is that the application can have their own urls.py file and we can call them from the project.
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index,name='index')
]