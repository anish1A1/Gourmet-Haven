import datetime
import os
from django.db import models
from django.contrib.auth.models import User


#2nd made
# in image field there is  get_file_path  we are creating a function of that
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S') # getting the current time and date
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/', filename)


# first this is made
class Category(models.Model):             #It inherits from models.Model, indicating that it's a Django model.
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null = True, blank = True)  #An ImageField field, which allows users to upload image files. 
    description = models.TextField(max_length=500, null = False, blank = False)
    status = models.BooleanField(default = False, help_text = "0=default, 1=Hidden")
    trending = models.BooleanField(default = False, help_text = "0=default, 1=Trending")
    meta_title = models.CharField(max_length =150, null=False, blank= False) 
    meta_keywords = models.CharField(max_length =150, null=False, blank= False)    
    meta_description = models.TextField(max_length=500, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)         #This field stores the date and time when the category was created.
    
    
    
    def __str__(self):           #This method returns a string representation of the category object.   #it will store the value
        return self.name                    
        

class Product(models.Model):
    category = models.name = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null = True, blank = True)  #An ImageField field, which allows users to upload image files. 
    small_description = models.CharField(max_length=250, null = False, blank = False)
    quantity = models.IntegerField(null = False, blank = False)
    description = models.TextField(max_length=500, null = False, blank = False)
    original_price = models.FloatField(null=False, blank = False)
    selling_price = models.FloatField(null=False, blank = False)
    status = models.BooleanField(default = False, help_text = "0=default, 1=Hidden")
    trending = models.BooleanField(default = False, help_text = "0=default, 1=Trending")
    tag= models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length =150, null=False, blank= False) 
    meta_keywords = models.CharField(max_length =150, null=False, blank= False)    
    meta_description = models.TextField(max_length=500, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)         #This field stores the date and time when the category was created.
    
    def __str__(self):           #This method returns a string representation of the category object.
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank= False)
    created_at = models.DateTimeField(auto_now_add=True)   