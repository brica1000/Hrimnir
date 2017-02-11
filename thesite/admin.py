from django.contrib import admin
from .models import Conglomerate, Product, Cert


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved_edit')  # Where does this understand the connection with Product?

class ConglomerateAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved_edit')
    
admin.site.register(Conglomerate, ConglomerateAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cert)
