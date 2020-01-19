from django.shortcuts import render

# Create your views here.
def index(request):
    data = {"personName":"Ryan"}
    return render(request, 'FittingApp/index.html', data)