from django.contrib import admin
from .models import Shipment


@admin.register(Shipment)
class ShipmentsAdmin(admin.ModelAdmin):
    fields = ('from_name', 'to_name', 'external_id')
    readonly_fields = fields
    list_display = fields
    list_display_links = fields
