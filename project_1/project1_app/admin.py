from django.contrib import admin
from .models import Data, Contact, Newsletter

# Register your models here.

admin.site.register(Data)
admin.site.register(Contact)
admin.site.register(Newsletter)