from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
# Create your views here.


def index(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products':products
    }
    return render(request,'core/index.html',context)

def product_list(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products':products
    }
    return render(request,'core/product_list.html',context)


def category_list_view(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories':categories
    }
    return render(request,'core/category_list.html',context)

