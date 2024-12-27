from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    phone_number=models.IntegerField(max_length=20)
    description=models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.product_name
