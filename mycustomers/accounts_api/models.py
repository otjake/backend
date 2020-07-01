from django.db import models

# Create your models here.

class Customers(models.Model): 
    customer_name        =   models.CharField(max_length=200, blank=True, null=True)  
    customer_email       =   models.CharField(max_length=200, blank=True, null=True)   
    customer_phone_number     =   models.IntegerField(blank=True, null=True)
    customer_acct_balance      =   models.IntegerField(blank=True, null=True)
    created_at          =   models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at          =   models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='customer', on_delete=models.CASCADE)


    class Meta:
            ordering = ["-created_at", "-updated_at"]        
            
    def __str__(self):
        return str(str(self.customer_name))
