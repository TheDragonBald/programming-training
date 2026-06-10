from django.contrib import admin
from .models import Request

# Register your models here.

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'subject', 'status', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('status',)
    readonly_fields = ('created_at',)
