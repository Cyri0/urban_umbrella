from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="static/logo/", null=True, blank=True)
    
    def __str__(self):
        return self.name

class ShopItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)

    gender_choices = [
        (0,'female'),
        (1,'male'),
        (3,'unisex')
    ]

    gender = models.IntegerField( choices = gender_choices )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    base_price = models.IntegerField()
    discount_percent = models.IntegerField()
    image = models.ImageField(upload_to="static/img/", null=True, blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name