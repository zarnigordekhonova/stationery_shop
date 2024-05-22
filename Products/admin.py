from django.contrib import admin
from .models import CategoryItems, ItemsMake, Items, Reviews
# Register your models here.

admin.site.register(CategoryItems)
admin.site.register(ItemsMake)
admin.site.register(Items)
admin.site.register(Reviews)