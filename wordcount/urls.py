from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('count2/', views.count, name='count'),
]
