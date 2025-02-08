from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)