from django.contrib import admin

# Register your models here.

from . import models

# Register your models here.

@admin.register(models.Annual)
class Annual(admin.ModelAdmin):
    list_display= [
        'annual'
    ]
    
    
@admin.register(models.Palace)
class Palace(admin.ModelAdmin):
    list_display = [
        'annual',
        'first_name',
        'last_name',
        'position'
    ]
    
    search_fields = (
        'annual',
        'first_name',
        'last_name',
        'position'
    )

@admin.register(models.Event)
class Event(admin.ModelAdmin):
    list_display = [
        'annual',
        'event_name',
        'event_location',
        'event_type'
    ]
    
    search_fields = (
        'annual',
        'event_name',
        'event_location',
        'event_type'
    )

@admin.register(models.Event_image)
class Event_image(admin.ModelAdmin):
    list_display = [
        'event',
        
    ]

@admin.register(models.Event_url)
class Event_url(admin.ModelAdmin):
    list_display = [
        'event',
        'url_name',
        'url'
    ]
    
    search_fields = (
        'event',
        'url_name'
    )