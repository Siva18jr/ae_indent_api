from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.CharField(max_length=50, null=False, blank=False)
    details = models.CharField(max_length=255, null=False, blank=False)
    category = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField()
    quantity = models.CharField(max_length=20, null=True, blank=False, default=1)
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


class Outlets(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    number = models.CharField(max_length=12, null=False, blank=False)
    storeId = models.CharField(max_length=20, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
    

class OutletProducts(models.Model):
    product_id = models.TextField(null=True)
    shift = models.IntegerField(null=False, blank=False)
    image_url = models.CharField(max_length=255)
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_price = models.CharField(max_length=50, null=False, blank=False)
    product_details = models.CharField(max_length=255, null=False, blank=False)
    product_category = models.CharField(max_length=50, null=False, blank=False)
    quantity = models.CharField(max_length=20, null=True, blank=False)
    date = models.CharField(max_length=50, null=False, blank=False)
    total_product_price = models.CharField(max_length=50, null=True, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.product_name} {self.shift}"
    

class RemainingProducts(models.Model):
    product_id = models.TextField(null=True)
    shift = models.IntegerField(null=False, blank=False)
    image_url = models.CharField(max_length=255)
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_price = models.CharField(max_length=50, null=False, blank=False)
    product_details = models.CharField(max_length=255, null=False, blank=False)
    product_category = models.CharField(max_length=50, null=False, blank=False)
    date = models.CharField(max_length=50, null=False, blank=False)
    total_product_price = models.CharField(max_length=50, null=True, blank=False)
    quantity = models.CharField(max_length=20, null=True, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.product_name} {self.shift}"
    

class SaleProducts(models.Model):
    product_details = models.TextField(null=True, blank=False)
    outlet_name = models.CharField(max_length=50, null=False, blank=False)
    outlet_location = models.CharField(max_length=50, null=False, blank=False)
    outlet_number = models.CharField(max_length=12, null=False, blank=False)
    outlet_store_id = models.CharField(max_length=20, null=False, blank=False)
    shift = models.IntegerField(null=True, blank=False)
    total = models.CharField(max_length=50, null=True, blank=False)
    cash = models.CharField(max_length=50, null=True, blank=False)
    date = models.CharField(max_length=50, null=True, blank=False)
    balance = models.CharField(max_length=50, null=True, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.outlet_name} {self.shift}"
    

class Users(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    password = models.CharField(max_length=50, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name