from django.contrib import admin
from products.models import Category, Product
'''
admin.site.register(Product)
admin.site.register(Category)
'''


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'image', 'description', 'created',
                    'height', 'width', 'manufacturer', 'reinforcement_material', 'power',
                    'armature_color', 'lighting_area', 'number_of_lamps']
    list_filter = ['created']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)