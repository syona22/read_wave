from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')  # or whatever field name you have
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.title
