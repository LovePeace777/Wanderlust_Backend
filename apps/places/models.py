from django.db import models
from apps.category.models import Category
from cloudinary.models import CloudinaryField
# Create your models here.

class Places(models.Model):

    name = models.CharField(
        'Name', blank=False, null=False, max_length=120, db_index=True
    )

    image = CloudinaryField(
        'image', blank=True, null=True
    )

    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )

    description = models.CharField(
        'description', blank=True, null=True, default='', max_length=50000
    )
    short_desc = models.CharField(
        'desc', blank=True, null=True, default='', max_length=10000
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, null=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, null=True, auto_now_add=True
    )
    
    def __str__(self):
        return self.name
