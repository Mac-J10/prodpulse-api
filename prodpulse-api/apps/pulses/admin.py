from django.contrib import admin
from .models import Pulse

@admin.register(Pulse)
class PulseAdmin(admin.ModelAdmin):
    list_display = ('product', 'timestamp', 'value', 'unit')
    list_filter = ('unit',)
    date_hierarchy = 'timestamp'
    search_fields = ('product__sku',)