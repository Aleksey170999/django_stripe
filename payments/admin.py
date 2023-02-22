from django.contrib import admin
from payments.models import Item


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price']
    list_display = ['name', 'description', 'price']


admin.site.register(Item, ItemAdmin)
