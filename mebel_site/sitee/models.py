from django.db import models

# Create your models here.
from mebel_site.sitee import price_choice, color_choice


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256)
    icon = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    price_type = models.CharField(max_length=5, choices=price_choice())
    color = models.CharField(max_length=64, choices=color_choice())
    size = models.JSONField(default={'len': 0, 'high': 0, 'eni': 0})
    short_description = models.TextField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


