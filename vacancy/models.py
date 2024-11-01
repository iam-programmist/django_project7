from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images')
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    typeofwork = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.created_at} - {self.is_active}'

class Application(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
