from django.contrib import admin
from .models import *

# Ver https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Admin_site#registrar_una_clase_modeladmin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)