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

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['title','image']
    search_fields = ['title','image']
    list_filter = ['title','image']
    inlines = [ProductImageInline]

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price']
    search_fields = ['user','price']
    list_filter = ['user','price']
    

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

admin.site.register(vendor,VendorAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Tags,TagsAdmin)
