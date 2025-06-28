from django.shortcuts import render
from django.http import HttpResponse
from core.models import *
from django.db.models import Count
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
    categories = Category.objects.all().order_by('-id').annotate(product_count=Count('category'))
    context = {
        'categories':categories
    }
    return render(request,'core/category_list.html',context)

def category_product_list_view(request,cid):
    category = Category.objects.get(cid=cid)
    
    products = Product.objects.filter(product_status='published',category=category).order_by('-id')
    context = {
        'category': category,
        'products':products
    }
    return render(request,'core/category_product_list.html',context)