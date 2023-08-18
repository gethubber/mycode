from django.contrib import admin
from .models import Todo

# the admin site has access to the Todo model
admin.site.register(Todo)

