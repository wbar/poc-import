from django.contrib import admin
from .models import ImportProcess, ImportProcessLog


class ImportProcessLogInlineAdmin(admin.TabularInline):
    model = ImportProcessLog
    fields = ('entry_date', 'level', 'message')
    readonly_fields = fields
    extra = 0
    ordering = ('entry_date', 'id')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ImportProcess)
class ImportProcessAdmin(admin.ModelAdmin):
    fields = ('thunder_id', 'start_date')
    readonly_fields = fields
    list_display = fields
    list_display_links = fields
    inlines = (ImportProcessLogInlineAdmin, )

    def has_add_permission(self, request):
        return False


