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
    p_images = product_obj.p_images.all()
    reviews = ProductReview.objects.filter(product=product_obj).order_by('-date')
    
    # Get related products from the same category (excluding current product)
    related_products = Product.objects.filter(
        category=product_obj.category,
        product_status='published'
    ).exclude(pid=product_obj.pid).order_by('-created_at')[:4]
    
    # Get new products (recently added)
    new_products = Product.objects.filter(
        product_status='published'
    ).exclude(pid=product_obj.pid).order_by('-created_at')[:4]
    
    # Get categories with product count
    categories = Category.objects.all().order_by('-id').annotate(product_count=Count('category'))
    
    # Calculate average rating
    if reviews.exists():
        avg_rating = sum(review.rating for review in reviews) / reviews.count()
        # Calculate rating distribution
        rating_distribution = {}
        for i in range(1, 6):
            rating_distribution[i] = reviews.filter(rating=i).count()
    else:
        avg_rating = 0
        rating_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    
    context = {
        'product':product_obj,
        'p_images':p_images,
        'reviews':reviews,
        'avg_rating':avg_rating,
        'rating_distribution':rating_distribution,
        'total_reviews':reviews.count(),
        'related_products':related_products,
        'new_products':new_products,
        'categories':categories
    }
    return render(request,'core/product_detail.html',context)

