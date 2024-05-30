from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('resist_calculator/', views.resist_calculator, name='resist_calculator'),
]