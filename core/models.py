from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


STATUS_CHOICES = (
    ("proccessing","Proccessing"),
    ("shipped","Shipped"),
    ("delivred","Delivred"),
)

STATUS = (
    ("draft","Draft"),
    ("disabled","DIsabled"),
    ("rejected","Rejected"),
    ("in_review","In Review"),
    ("published","Published"),
)

RATING = (
    (1,"⭐"),
    (2,"⭐⭐"),
    (3,"⭐⭐⭐"),
    (4,"⭐⭐⭐⭐"),
    (5,"⭐⭐⭐⭐⭐"),
)




def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def product_directory_path(instance, filename):
    return 'products/{0}/{1}'.format(instance.pid, filename)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10,max_length=30 , prefix="cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="category")
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.img.url))
    
    def __str__(self):
        return self.title
    
    
class vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10,max_length=30 , prefix="ven",alphabet="abcdefgh12345")
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=user_directory_path)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True) 
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    chat_resp_time = models.CharField(max_length=120, blank=True,default="24 hours")
    phone = models.CharField(max_length=120, blank=True,default="0123456789")
    authetic_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    days_return = models.IntegerField(default=0)
    waranty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    class Meta:
        verbose_name = 'vendor'
        verbose_name_plural = 'vendors'
        
    
        
class Tags(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10,max_length=30 , prefix="pro",alphabet="abcdefgh12345")
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=product_directory_path)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    old_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    in_stock = models.BooleanField(default=True)
    feutured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    vendor = models.ForeignKey(vendor, on_delete=models.SET_NULL, null=True)
    specification = models.TextField(blank=True,null=True)
    tags = models.ManyToManyField(Tags, blank=True)
    product_status = models.CharField(choices=STATUS,max_length=10,default='in_review')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    sku = ShortUUIDField(unique=True, length=10,max_length=30 , prefix="sku",alphabet="abcdefgh12345")
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return new_price

class ProductReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL ,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL ,null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING , default = None)
    date = models.DateTimeField(auto_now_add = True)

    class Meta :
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title
    def get_rating(self):
        return self.rating


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'
        

class CartOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICES,max_length=30,default='proccessing')
    
    class Meta:
        verbose_name = 'cart order'
        verbose_name_plural = 'cart orders'
        
    def __str__(self):
        return self.user.username
    
class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    product_status = models.CharField(choices=STATUS_CHOICES,max_length=30,default='proccessing')
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    
    class Meta:
        verbose_name = 'cart order item'
        verbose_name_plural = 'cart order items'
        
    def __str__(self):
        return self.order.user.username
    
    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    
    
    
    
