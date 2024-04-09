from django.contrib import admin
from .models import Category, Product, ProductImage, ProductComment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon_url', 'created_at', 'updated_at', 'deleted_at')
    search_fields = ('name', 'slug')
    list_filter = ('created_at', 'updated_at', 'deleted_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'price', 'discount', 'amount', 'is_public', 'thumbnail', 'category_id', 'created_at', 'updated_at', 'deleted_at')
    search_fields = ('name', 'unit', 'category_id__name')
    list_filter = ('is_public', 'created_at', 'updated_at', 'deleted_at')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'product_id', 'created_at', 'updated_at', 'deleted_at')
    search_fields = ('product_id__name',)
    list_filter = ('created_at', 'updated_at', 'deleted_at')

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('rating', 'comment', 'product_id', 'parent_id', 'created_at', 'updated_at', 'deleted_at', 'user_id')
    search_fields = ('product_id__name', 'comment')
    list_filter = ('rating', 'created_at', 'updated_at', 'deleted_at', 'user_id')
