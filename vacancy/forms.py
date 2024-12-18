from django import forms
from .models import Country, City, CustomUser, Profile, VacancyCategory, Vacancy, Application, Favorite, Response, Message

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['country','name']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'role', 'country', 'city', 'phone_number', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'resume', 'profile_picture']

class VacancyCategoryForm(forms.ModelForm):
    class Meta:
        model = VacancyCategory
        fields = ['name']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['vacancy_category', 'user', 'title', 'image', 'description', 'salary', 'type_of_work']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['user', 'country', 'city', 'message']

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['user', 'vacancy', 'worker']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['application', 'response_message']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'recipient', 'content']