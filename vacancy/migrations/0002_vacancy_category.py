# Generated by Django 4.2.16 on 2024-11-01 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancy.category'),
        ),
    ]
