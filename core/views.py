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

