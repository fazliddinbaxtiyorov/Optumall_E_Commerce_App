from django.contrib import admin
from .models import Users, Products, Profile, Cart

# Register your models here.
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Profile)
admin.site.register(Cart)
