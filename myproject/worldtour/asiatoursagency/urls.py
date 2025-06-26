from django.urls import path
from . import views

#define a list of url pattern
urlpatterns =[
    path('',views.index)
]