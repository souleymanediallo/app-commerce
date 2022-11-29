from django.db import models


# Create your models here.
class Slider(models.Model):
    DISCOUNT_DEAL = (
        ('HOT DEALS', 'HOT DEALS'),
        ('NEW ARRIVALS', 'NEW ARRIVALS'),
    )

    image = models.ImageField(upload_to='media/slider'),
    discount_deal = models.CharField(choices=DISCOUNT_DEAL, max_length=100),
    sale = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    discount = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class MainCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.main_category.name} -- {self.name}"


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category.main_category.name} -- {self.category.name} -- {self.name}"


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    feature_image = models.ImageField(upload_to='product/')
    quantity = models.IntegerField()
    availability = models.IntegerField()
    discount = models.IntegerField()
    tags = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to='product/')


class AdditionalInformation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.CharField(max_length=200)
    detail = models.CharField(max_length=100)