from django.db import models

from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.text import slugify

FLAG_TYPE=(

    ('new','new'),
    ('sale','sale'),
    ('feature','feature'),
)

class Products(models.Model):
    ''' Products table '''


    name = models.CharField('name',max_length=120)
    flag = models.CharField(max_length=10,choices=FLAG_TYPE)
    price =models.FloatField()
    image=models.ImageField(upload_to='product')
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=500)
    description = models.TextField(10000) 
    tags = TaggableManager()
    slug = models.SlugField(blank=True,null=True,unique=True)
    
    brand = models.ForeignKey('Brand',related_name='product_brand',on_delete=models.CASCADE)


    def save(self , *args,**kwargs):
        self.slug = slugify(self.name)
        super(Products,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.name)
    

class ProductImages(models.Model):
    pruduct = models.ForeignKey(Products,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')



class Brand(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='brand')

    slug = models.SlugField(blank=True,null=True,unique=True)



    def save(self , *args,**kwargs):
        self.slug = slugify(self.name)
        super(Brand,self).save(*args,**kwargs)



class Reviews(models.Model):
    user = models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Products,related_name='review_product', on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(choices=[(i,i) for i in range(1,6)])

    created_at = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rate}"


