from django.contrib import admin
from .models import *


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1

class ProductPhotoAdmin(admin.ModelAdmin):
    inlines = [ProductPhotoInline]


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Product, ProductPhotoAdmin)
admin.site.register(Rating)
admin.site.register(Review)
