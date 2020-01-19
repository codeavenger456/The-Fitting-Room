from django.urls import path 
from . import views

app_name = "FittingApp"

urlpatterns = [
    path('<str:name>/<str:gender>/<int:height>/<str:season>/<usage>', views.index, name = "index"),
    #path('', views.index, name = "final"),
]