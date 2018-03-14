from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import Product, ProductCategory


class ProductAdmin(ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    menu_icon = 'fa-desktop'
    menu_label = 'Products'
    model = Product


class ProductCategoryAdmin(ModelAdmin):
    menu_icon = 'fa-object-group'
    menu_label = 'Categories'
    model = ProductCategory


class ProductAdminGroup(ModelAdminGroup):
    menu_icon = 'fa-car'
    menu_label = 'Products'
    items = [ProductAdmin, ProductCategoryAdmin]


modeladmin_register(ProductAdminGroup)
