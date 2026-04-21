from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Meowy 🐱")

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {
        'products': products
    })
