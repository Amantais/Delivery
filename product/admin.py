from django.contrib import admin

from .models import Category, Product, ProductImage, MainComment 

class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2 
    fields = ['image']



class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
    list_display = ('uuid', 'title', 'price')
    list_display_links = ('uuid', 'title')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(MainComment)