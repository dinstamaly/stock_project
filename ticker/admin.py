from django.contrib import admin

from .models import History, Ticker
# Register your models here.

admin.site.register(History)
admin.site.register(Ticker)
