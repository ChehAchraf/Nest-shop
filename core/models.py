from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    cid = ShortUUIDField(unique=True, lenght=10,max_length=30 , prefix="cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to="category")
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.img.url))
    
    def __str__(self):
        return self.title
    
    
class vendor(models.model):
    vid = ShortUUIDField(unique=True, lenght=10,max_length=30 , prefix="ven",alphabet="abcdefgh12345")
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to=user_directory_path)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True) 
    description = models.TextField(blank=True)
    address = models.TextField(blank=True)
    chat_resp_time = models.CharField(max_length=120, blank=True,default="24 hours")
    phone = models.CharField(max_length=120, blank=True,default="0123456789")
    authetic_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    days_return = models.IntegerField(default=0)
    waranty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'vendor'
        verbose_name_plural = 'vendors'
        
    
