from django import forms
from .models import Category ,Vacancy, Application

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'image', 'description', 'salary', 'typeofwork']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']