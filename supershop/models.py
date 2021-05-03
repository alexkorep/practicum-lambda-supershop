from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from django.core.validators import MinValueValidator

class Product(TimeStampedModel):
    name = models.CharField(_('название'), max_length=255)
    description = models.TextField(_('описание'), blank=True)

    class Meta:
        verbose_name = _('продукт')
        verbose_name_plural = _('продукты')

    def __str__(self):
        return self.name

class Order(TimeStampedModel):
    customer_name = models.CharField(_('имя заказчика'), max_length=255)
    customer_address = models.TextField(_('адрес заказчика'), blank=False)
    creation_date = models.DateField(_('дата создания заказа'), blank=True)

    class Meta:
        verbose_name = _('заказ')
        verbose_name_plural = _('заказы')

    def __str__(self):
        return self.customer_name 

class OrderProduct(models.Model):
    class Meta:
        unique_together = ('order', 'product',)

    quantity = models.IntegerField(_('количество'), null=False) 
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField(_('имя актера'), max_length=255)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(_('название фильма'), max_length=255)
    actors = models.ManyToManyField('Actor')
    def __str__(self):
        return self.title

