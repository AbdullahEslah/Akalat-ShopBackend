from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'restaurant')
    name = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    logo = models.ImageField(upload_to = 'restaurant_logos/', blank = True) #blank means not required

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='meal_images/', blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):

    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERD = 4

    STATUS_CHOICES = (
    (COOKING, "Cooking"),
    (READY, "Ready"),
    (ONTHEWAY, "On the way"),
    (DELIVERD, "Deliverd"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    driver = models.ForeignKey(Driver, models.SET_NULL, blank = True, null = True)
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.IntegerField(choices = STATUS_CHOICES)
    created_at = models.DateTimeField(default = timezone.now)
    picked_at = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return str(self.id)

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_details')
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    def __str__(self):
        return str(self.id)
