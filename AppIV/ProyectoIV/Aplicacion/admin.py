from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Enterprise, Calification

admin.site.register(Enterprise)
admin.site.register(Calification)