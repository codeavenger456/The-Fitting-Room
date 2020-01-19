from django.urls import path 
from . import views

app_name = "FittingApp"

urlpatterns = [
    path('<str:name>/<str:gender>/<int:height>', views.index, name = "index"),
]