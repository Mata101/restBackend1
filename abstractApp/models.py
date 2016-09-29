from django.db import models




class Client(models.Model):
    username = models.CharField(max_length=250,null='FALSE')
    password = models.CharField(max_length=250,null='FALSE')
    homeadd = models.CharField(max_length=250,null='FALSE')
    def __str__(self):
        return self.username
class Admin(models.Model):
    username = models.CharField(max_length=250,null='FALSE')
    password = models.CharField(max_length=250,null='FALSE')
    
    def __str__(self):
        return self.username
class Product(models.Model):
    
    product_name = models.CharField(max_length=250,null='FALSE')
    product_price = models.DecimalField(max_digits=250,decimal_places=2,null='FALSE')
    
    product_type = models.CharField(max_length=250,null='FALSE')
    def __str__(self):
        return self.product_name + " - " + self.product_price

class History(models.Model):
    clientid = models.CharField(max_length=250,null='FALSE')
    product_id=models.CharField(max_length=250,null='FALSE')
   
    quantity =models.IntegerField(null='FALSE')
    time = models.TimeField(max_length=250,null='FALSE')
    date = models.DateField(max_length=250,null='FALSE')
    
    def __str__(self):
        return self.product_name + " - " + self.product_price

class Order(models.Model):
    clientid = models.CharField(max_length=250,null='FALSE')
    product_id=models.CharField(max_length=250,null='FALSE')
    
    quantity =models.CharField(max_length=250,null='FALSE')
    time = models.TimeField(max_length=250,null='FALSE')
    date = models.DateField(max_length=250,null='FALSE')
    

    def __str__(self):
        return self.product_name + " - " + self.product_price