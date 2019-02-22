from django.contrib import admin
from django.urls import path
from basic_app import views

#TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('lesson/',views.lesson,name='lesson'),
    path('other/',views.other,name='other'),
]
