# Generated by Django 4.1.6 on 2023-03-03 13:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebPortfolioApp', '0005_remove_portfoliostructure_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliostructure',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='portfoliostructure',
            name='like',
        ),
        migrations.AddField(
            model_name='portfoliostructure',
            name='likes',
            field=models.ManyToManyField(related_name='project_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
