from django.contrib import admin

# Register your models here - make databases visible in admin panel
from .models import Room

admin.site.register(Room)