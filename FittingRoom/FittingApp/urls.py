from django.urls import path 
from . import views

app_name = "FittingApp"

urlpatterns = [
    path('', views.index, name = "index")
]