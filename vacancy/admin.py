from django.contrib import admin
from .models import Country, City, CustomUser, Profile, VacancyCategory, Vacancy, Application

admin.site.register(Country)
admin.site.register(City)
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(VacancyCategory)
admin.site.register(Vacancy)
admin.site.register(Application)