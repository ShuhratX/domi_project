from django.contrib import admin
from .models import (
    Manufacturer,
    Category,
    SubCategory,
    Smartphone,
    Notebook,
    TV_product,
    Planshet
)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_category')

    def get_category(self, obj):
        return obj.category.title

    get_category.short_description = 'Kategoriyalar'


class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'get_subcategory', 'description', 'diagonal', 'display_type', 'rom', 'ram', 'main_cam_mp', 'front_cam_mp')
    def get_subcategory(self, obj):
        return obj.subcategory.title

    get_subcategory.short_description = 'Subategoriyasi'


class PlanshetAdmin(admin.ModelAdmin):
    list_display = (
    'title', 'price', 'get_subcategory', 'description', 'diagonal', 'display_type', 'rom', 'ram', 'main_cam_mp',
    'front_cam_mp')

    def get_subcategory(self, obj):
        return obj.subcategory.title

    get_subcategory.short_description = 'Subategoriyasi'


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Planshet, PlanshetAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
