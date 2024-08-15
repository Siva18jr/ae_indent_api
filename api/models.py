from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.CharField(max_length=50, null=False, blank=False)
    details = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Outlet(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    number = models.CharField(max_length=12, null=False, blank=False)
    storeId = models.CharField(max_length=20, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name