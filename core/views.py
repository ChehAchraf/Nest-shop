from django.shortcuts import render, get_object_or_404
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

def vendor_list_view(request):
    vendors = vendor.objects.all().order_by('-id')
    context = {
        'vendors':vendors
    }
    return render(request,'core/vendor_list.html',context)


def vendor_detail_view(request,vid):
    vendor_obj = get_object_or_404(vendor, vid=vid)
    context = {
        'vendor':vendor_obj
    }
    return render(request,'core/vendor_detail.html',context)


def product_detail_view(request,pid):
    product_obj = get_object_or_404(Product, pid=pid)
    context = {
        'product':product_obj
    }
    return render(request,'core/product_detail.html',context)

