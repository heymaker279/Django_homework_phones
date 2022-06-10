from django.db import models
from django.urls import reverse
# Create your models here.



class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=20)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'slug': self.slug})