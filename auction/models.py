from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey("custom_auth.User", on_delete=models.CASCADE)
    images = ArrayField(
        models.URLField(null=True, blank=True),
        null=True, 
        blank=True
     )
    category = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True,blank=True)
    end_time = models.TimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey("custom_auth.User")
    price = models.DecimalField(max_digits=16, decimal_places=2, help_text="Amount in INR.")
    is_won = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    