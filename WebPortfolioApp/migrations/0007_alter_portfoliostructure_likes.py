# Generated by Django 4.1.6 on 2023-03-03 14:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebPortfolioApp', '0006_remove_portfoliostructure_dislike_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliostructure',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
