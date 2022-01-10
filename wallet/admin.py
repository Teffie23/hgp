from django.contrib import admin
from .models import *
class usersAdmin(admin.ModelAdmin):
    list_display=('id','title',)
    list_display_links=('id','title',)
    search_fields =('title','content')
    prepopulated_fields = {'slug': ('title',)}
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'names')
    list_display_links = ('id', 'names')
    search_fields = ('names', 'buy')
    prepopulated_fields = {'slug': ('names',)}
class ApdataAdmin(admin.ModelAdmin) :
    list_display = ('id','title','content','data')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Apdata,ApdataAdmin)
admin.site.register(users,usersAdmin)
# Register your models here.
admin.site.site_title='Админ-панель сайта о женщинах'
admin.site.site_header='Админ-панель банка'
# Register your models here.
