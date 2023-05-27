import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Basemodel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    creator = models.ForeignKey(User, blank=True,related_name="creator_%(class)s_objects",on_delete=models.CASCADE)
    updater = models.ForeignKey(User, blank=True,null=True,related_name="updater_%(class)s_objects",on_delete=models.CASCADE)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)    
    date_updated = models.DateTimeField(auto_now_add=True)  
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Category(Basemodel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('category')
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.name


class Products(Basemodel):
    name = models.CharField(max_length=255, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    mrp = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(0)])
    image = models.ImageField(upload_to='products')
    is_active = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)

    class Meta:
        db_table = 'products'
        ordering = ('category',)

    def __str__(self):
        return str(self.category)