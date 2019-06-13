from django.contrib import admin
from .models import Document, Product
# Register your models here.
admin.site.register([Document, Product])