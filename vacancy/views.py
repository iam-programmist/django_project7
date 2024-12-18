from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth import get_user_model
from .models import *
from .forms import *

class CountryListView(ListView):
    model = Country
    template_name = 'country_list.html'
    context_object_name = 'countries'

class CountryDetailView(DetailView):
    model = Country
    template_name = 'country_detail.html'
    context_object_name = 'country'

class CountryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'country_form.html'
    success_url = reverse_lazy('country-list')

    def test_func(self):
        return self.request.user.is_superuser

class CountryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'country_form.html'
    success_url = reverse_lazy('country-list')

    def test_func(self):
        return self.request.user.is_superuser

class CountryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Country
    template_name = 'country_confirm_delete.html'
    success_url = reverse_lazy('country-list')

    def test_func(self):
        return self.request.user.is_superuser

class CityListView(ListView):
    model = City
    template_name = 'city_list.html'
    context_object_name = 'cities'

class CityDetailView(DetailView):
    model = City
    template_name = 'city_detail.html'
    context_object_name = 'city'

class CityCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'city_form.html'
    success_url = reverse_lazy('city-list')

    def test_func(self):
        return self.request.user.is_superuser

class CityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'city_form.html'
    success_url = reverse_lazy('city-list')

    def test_func(self):
        return self.request.user.is_superuser

class CityDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = City
    template_name = 'city_confirm_delete.html'
    success_url = reverse_lazy('city-list')

    def test_func(self):
        return self.request.user.is_superuser
    
class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        if self.request.user.is_employer():
            return CustomUser.objects.filter(role='worker')
        return CustomUser.objects.filter(role='employer')

class CustomUserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_queryset(self):
        if self.request.user.is_employer():
            return CustomUser.objects.filter(role='worker')
        return CustomUser.objects.filter(role='employer')
    
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_detail.html'
    context_object_name = 'profile'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_form.html'
    success_url = reverse_lazy('profile-detail')

    def get_object(self):
        return self.request.user.profile
    
class VacancyCategoryListView(ListView):
    model = VacancyCategory
    template_name = 'vacancy_category_list.html'
    context_object_name = 'categories'

class VacancyCategoryDetailView(DetailView):
    model = VacancyCategory
    template_name = 'vacancy_category_detail.html'
    context_object_name = 'category'

class VacancyCategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = VacancyCategory
    form_class = VacancyCategoryForm
    template_name = 'vacancy_category_form.html'
    success_url = reverse_lazy('vacancy-category-list')

    def test_func(self):
        return self.request.user.is_superuser

class VacancyCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VacancyCategory
    form_class = VacancyCategoryForm
    template_name = 'vacancy_category_form.html'
    success_url = reverse_lazy('vacancy-category-list')

    def test_func(self):
        return self.request.user.is_superuser

class VacancyCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VacancyCategory
    template_name = 'vacancy_category_confirm_delete.html'
    success_url = reverse_lazy('vacancy-category-list')

    def test_func(self):
        return self.request.user.is_superuser
    
class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy_list.html'
    context_object_name = 'vacancies'

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancy_detail.html'
    context_object_name = 'vacancy'

class VacancyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancy_form.html'
    success_url = reverse_lazy('vacancy-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_employer()

class VacancyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancy_form.html'
    success_url = reverse_lazy('vacancy-list')

    def test_func(self):
        vacancy = self.get_object()
        return self.request.user == vacancy.user and self.request.user.is_employer()

class VacancyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vacancy
    template_name = 'vacancy_confirm_delete.html'
    success_url = reverse_lazy('vacancy-list')

    def test_func(self):
        vacancy = self.get_object()
        return self.request.user == vacancy.user and self.request.user.is_employer()

class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'application_list.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'application_detail.html'
    context_object_name = 'application'

class ApplicationCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_worker()

class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Application
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('application-list')

    def test_func(self):
        application = self.get_object()
        return self.request.user == application.user and self.request.user.is_worker()

class FavoriteListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'favorite_list.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class FavoriteCreateView(LoginRequiredMixin, CreateView):
    model = Favorite
    form_class = FavoriteForm
    template_name = 'favorite_form.html'
    success_url = reverse_lazy('favorite-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ResponseListView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'response_list.html'
    context_object_name = 'responses'

    def get_queryset(self):
        return Response.objects.filter(application__user=self.request.user)

class ResponseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'response_form.html'
    success_url = reverse_lazy('response-list')

    def test_func(self):
        return self.request.user.is_employer()

class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user) | Message.objects.filter(sender=self.request.user)

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message-list')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)