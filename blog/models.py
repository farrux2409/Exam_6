from django.db import models


# Create your models here.

class Product(models.Model):
    class RatingChoice(models.IntegerChoices):
        Zero = 0
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    rating = models.IntegerField(choices=RatingChoice.choices, default=RatingChoice.Zero.value)
    amount = models.IntegerField(default=1)
    discount = models.IntegerField()
    attribute =models.ManyToManyField('Attribute', blank=True, null=True, related_name='attribute')

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey('blog.Product', on_delete=models.CASCADE, related_name='images')


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=100)

    def __str__(self):
        return self.attribute_name

class Customer(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    billing_address = models.TextField()
    joined_date = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
        




