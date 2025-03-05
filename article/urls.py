from django.contrib import admin
from django.urls import path,include

#from article.views import index
from . import views

app_name = "article"

urlpatterns = [
    path('',views.index,name="index"),
    path('create/', views.index, name="index"),

]
