from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancy/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('vacancy/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    path('vacancy/<int:pk>/delete/', VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('applications/', ApplicationListView.as_view(), name='application_list'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application_detail'),
    path('application/create/', ApplicationCreateView.as_view(), name='application_create'),
    path('application/<int:pk>/update/', ApplicationUpdateView.as_view(), name='application_update'),
    path('application/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application_delete'),
]
