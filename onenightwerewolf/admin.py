from django.contrib import admin
from .models import NameModel, NumberModel

# Register your models here.

admin.site.register(NameModel)
admin.site.register(NumberModel)