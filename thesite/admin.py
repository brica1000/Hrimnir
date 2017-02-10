from django.contrib import admin
from .models import Conglomerate, Product, Cert


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved_edit')

admin.site.register(Conglomerate)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cert)
