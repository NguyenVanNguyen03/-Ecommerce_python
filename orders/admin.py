from django.contrib import admin
from .models import Order, OrderDetail

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'receiver_name', 'receiver_phone', 'receiver_address', 'is_ordered', 'is_paid', 'total', 'created_at', 'updated_at')
    list_filter = ('is_ordered', 'is_paid', 'created_at')
    search_fields = ('receiver_name', 'receiver_phone', 'receiver_address', 'description')
    inlines = [OrderDetailInline]

admin.site.register(Order, OrderAdmin)
