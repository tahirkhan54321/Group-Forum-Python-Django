# This file is used to customize the built-in Django admin interface, 
# where you can register your models 
# and configure how they should be displayed and edited.

from django.contrib import admin

# Register your models here - make databases visible in admin panel
from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)