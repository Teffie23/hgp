from django.db import models
from django.urls import reverse, reverse_lazy
from autoslug import AutoSlugField
class users(models.Model):
    title=models.CharField(max_length=255,verbose_name='Имя')
    balance=models.FloatField(verbose_name='Баланс')
    currency=models.CharField(max_length=3,verbose_name='Валюта')
    slug = AutoSlugField(max_length=255, unique=True, db_index=True, verbose_name='URL',populate_from='balance')
    data=models.DateTimeField(auto_now_add=True)
    currency=models.ForeignKey('Currency', on_delete=models.PROTECT,verbose_name='Валюта')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('hummen',kwargs={'hummen_slug':self.slug})
    class Meta:
        verbose_name='Пользователи'
        verbose_name_plural='Пользователи'
        ordering=['title',]
class Currency(models.Model):
    names=models.CharField(max_length=3, verbose_name='название')
    buy=models.FloatField(verbose_name='Цена')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.names
    def get_absolute_url(self):
        return reverse('cur', kwargs={'cur_slug': self.slug})
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'
class Apdata(models.Model):
    title=models.CharField(max_length=255,verbose_name='Заголовок')
    content=models.TextField()
    data=models.DateTimeField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})
    class Meta:
        verbose_name='История'
        verbose_name_plural='История'
# Create your models here.
