from django.contrib import admin
from .models import Category, Vacancy, Application

admin.site.register(Category)
admin.site.register(Vacancy)
admin.site.register(Application)