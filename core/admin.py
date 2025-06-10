from django.contrib import admin
from .models import *
# Register your models here.


class VendorAdmin(admin.ModelAdmin):
    list_display = ['name','phone']
    search_fields = ['name','phone']
    list_filter = ['name','phone']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title','image']
    list_filter = ['title','image']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title','image']
    list_filter = ['title','image']

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price']
    search_fields = ['user','price']
    list_filter = ['user','price']










admin.site.register(vendor,VendorAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(ProductImage)

