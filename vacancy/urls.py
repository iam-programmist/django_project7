from django.urls import path
from .views import *

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('countries/create/', CountryCreateView.as_view(), name='country-create'),
    path('countries/update/<int:pk>/', CountryUpdateView.as_view(), name='country-update'),
    path('countries/delete/<int:pk>/', CountryDeleteView.as_view(), name='country-delete'),

    path('cities/', CityListView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
    path('cities/create/', CityCreateView.as_view(), name='city-create'),
    path('cities/update/<int:pk>/', CityUpdateView.as_view(), name='city-update'),
    path('cities/delete/<int:pk>/', CityDeleteView.as_view(), name='city-delete'),

    path('users/', CustomUserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),

    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),

    path('vacancy-categories/', VacancyCategoryListView.as_view(), name='vacancy-category-list'),
    path('vacancy-categories/<int:pk>/', VacancyCategoryDetailView.as_view(), name='vacancy-category-detail'),
    path('vacancy-categories/create/', VacancyCategoryCreateView.as_view(), name='vacancy-category-create'),
    path('vacancy-categories/update/<int:pk>/', VacancyCategoryUpdateView.as_view(), name='vacancy-category-update'),
    path('vacancy-categories/delete/<int:pk>/', VacancyCategoryDeleteView.as_view(), name='vacancy-category-delete'),

    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy-create'),
    path('vacancies/update/<int:pk>/', VacancyUpdateView.as_view(), name='vacancy-update'),
    path('vacancies/delete/<int:pk>/', VacancyDeleteView.as_view(), name='vacancy-delete'),

    path('applications/', ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('applications/create/', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/delete/<int:pk>/', ApplicationDeleteView.as_view(), name='application-delete'),

    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/create/', FavoriteCreateView.as_view(), name='favorite-create'),

    path('responses/', ResponseListView.as_view(), name='response-list'),
    path('responses/create/', ResponseCreateView.as_view(), name='response-create'),

    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),
]
