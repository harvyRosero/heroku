from enum import unique
from django.db import models
from  django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    resumen = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='images/blog')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
    

def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        
pre_save.connect(pre_save_product_receiver, sender=Post)