from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


#Creating model for listing
class Listing(models.Model):
    seller = models.CharField(max_length = 64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    staring_bid = models.IntegerField()
    category = models.CharField(max_length=64)
    image_link = models.CharField(max_length=200 , default=none , blank=True , null=True , created_at = models.DateTimeField(auto_now_add=True))
    
#Model for bids
class Bid(models.Model): 
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listingbid = models.IntegerField()
    bid = models.IntegerField()
    
    
#Model for comments 
class Comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=64)
    listingbid = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
#Model for Watchlist
class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.IntegerField()
    
#Model to Store the Winners
class Winner(models.Model) :
    owner = models.CharField(max_length=64)
    Winner = models.CharField(max_length=64)
    listingid = models.IntegerField()
    winprice = models.IntegerField()
    title = models.CharField(max_length=64 , null=True)