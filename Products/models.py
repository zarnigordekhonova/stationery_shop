from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Customers.models import CustomUser
# Create your models here.

class CategoryItems(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.name


class ItemsMake(models.Model):
    make = models.CharField(max_length=64)

    class Meta:
        db_table = 'Make'

    def __str__(self):
        return self.make

class Items(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(CategoryItems, on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField()
    characteristics = models.TextField()
    make = models.ForeignKey(ItemsMake, on_delete=models.DO_NOTHING, default=' ')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, default='not_available.png')


    class Meta:
        db_table = 'Products'

    def __str__(self):
        return f'{self.name}'


class Reviews(models.Model):
    comment = models.TextField()
    star_given = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    product_name = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)


    class Meta:
        db_table = 'Reviews'

    def __str__(self):
        return f'{self.star_given}'