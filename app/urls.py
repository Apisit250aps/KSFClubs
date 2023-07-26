from django.contrib import admin
from django.urls import path

from . import views as app

urlpatterns = [
    path('', app.page, name='index'),
    path('staff/', app.staff_palace, name='staff-palace'),
]
