from django.db import models
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.country.name}'

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('worker', 'Worker'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='worker')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=150, unique=True)

    def is_employer(self):
        return self.role == 'employer'

    def is_worker(self):
        return self.role == 'worker'

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='media/resumes', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'

class VacancyCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    vacancy_category = models.ForeignKey(VacancyCategory, on_delete=models.CASCADE, related_name='vacancies')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='vacancies')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/vacancy_images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    salary = models.CharField(max_length=50, null=True, blank=True, default='negotiable')
    type_of_work = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.user.username} - {self.created_at} - {self.is_active}'

    def save(self, *args, **kwargs):
        if not self.user.is_employer():
            raise ValueError("Only employers can create vacancies.")
        super().save(*args, **kwargs)

class Application(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='applications')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='applications')
    message = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.message} - {self.user.username}'

    def save(self, *args, **kwargs):
        if not self.user.is_worker():
            raise ValueError("Only employees can create requests.")
        super().save(*args, **kwargs)

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorites')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True, blank=True, related_name='favorites')
    worker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='favorited_by')

    def __str__(self):
        if self.vacancy:
            return f'{self.user.username} added {self.vacancy.title} to favorites'
        return f'{self.user.username} added {self.worker.username} to favorites'

    def save(self, *args, **kwargs):
        if self.user.is_employer() and not self.worker:
            raise ValueError("Employers can only favorite workers.")
        if self.user.is_worker() and not self.vacancy:
            raise ValueError("Workers can only favorite vacancies.")
        super().save(*args, **kwargs)

class Response(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='responses')
    response_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Response to {self.application.user.username} - {self.created_at}'

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username} at {self.timestamp}'

    def save(self, *args, **kwargs):
        if self.sender.is_employer() and self.recipient.is_employer():
            raise ValueError("Employers cannot message other employers.")
        if self.sender.is_worker() and self.recipient.is_worker():
            raise ValueError("Workers cannot message other workers.")
        super().save(*args, **kwargs)
