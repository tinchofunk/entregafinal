from django.contrib import admin

from .models import *  # importamos el archivo models


admin.site.register(Productos)
admin.site.register(Cliente)
admin.site.register(Stock)
