from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy_list.html'

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy_detail.html'

class VacancyCreateView(CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancy_form.html'
    success_url = reverse_lazy('vacancy_list')

class VacancyUpdateView(UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancy_form.html'
    success_url = reverse_lazy('vacancy_list')

class VacancyDeleteView(DeleteView):
    model = Vacancy
    template_name = 'vacancy_confirm_delete.html'
    success_url = reverse_lazy('vacancy_list')

class ApplicationListView(ListView):
    model = Application
    template_name = 'application_list.html'

class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'application_detail.html'

class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application_list')

class ApplicationUpdateView(UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application_list')

class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('application_list')
