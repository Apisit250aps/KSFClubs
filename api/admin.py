from django.contrib import admin

# Register your models here.

from . import models

# Register your models here.

@admin.register(models.Annual)
class Annual(admin.ModelAdmin):
    list_display= [
        'annual'
    ]


@admin.register(models.palace)
class Character(admin.ModelAdmin):
    list_display = [
        'annual',
        'first_name',
        'last_name',
        'position'
    ]

@admin.register(models.event)
class Character(admin.ModelAdmin):
    list_display = [
        'annual',
        'event_name',
        'event_location',
        'event_type'
    ]

@admin.register(models.event_image)
class Character(admin.ModelAdmin):
    list_display = [
        'event',
        
    ]

@admin.register(models.event_url)
class Character(admin.ModelAdmin):
    list_display = [
        'event',
    ]