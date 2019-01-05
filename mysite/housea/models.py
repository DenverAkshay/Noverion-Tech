from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from geoposition.fields import GeopositionField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.
class Tenant(models.Model):
    GENDER_CHOICE={
        ('male','Male'), ('female','Female')
    }
    name = models.CharField(max_length=40,unique=True)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default= 'male' )
    slug = models.SlugField(max_length=60)
    mobile_1 = models.CharField(max_length=12,unique=True)
    mobile_2 = models.CharField(max_length=12,unique=True)
    mobile_3 = models.CharField(max_length=12,unique=True)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length = 30)
    created_on = models.DateTimeField(default = timezone.now)
    location = GeopositionField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tenant-detail',args = [self.id ,self.slug])

@receiver(pre_save,sender=Tenant)
def pre_save_slug(sender,**kwargs):
    slug = slugify(kwargs['instance'].name)
    kwargs['instance'].slug = slug
