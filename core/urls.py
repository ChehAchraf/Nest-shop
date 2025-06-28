from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    #home page
    path('',views.index, name="index"),
    #product list
    path('products/',views.product_list, name="product_list"),
    #category list
    path('categories/',views.category_list_view, name="category_list"),
    #category product list
    path('categories/<str:cid>/',views.category_product_list_view, name="category_product_list"),
    #vendor list
    path('vendors/',views.vendor_list_view, name="vendor_list"),
    #vendor detail
    path('vendors/<str:vid>/',views.vendor_detail_view, name="vendor_detail"),
    #product detail
    path('product/<str:pid>/',views.product_detail_view, name="product_detail"),
    #search
    path('search/',views.search_view, name="search"),
]