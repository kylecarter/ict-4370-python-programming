from django.contrib import admin
from .models import Stock

# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display=['pk', 'symbol', 'date']


admin.site.register(Stock, StockAdmin)
