# Generated by Django 4.1.6 on 2023-03-02 17:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebPortfolioApp', '0004_portfoliostructure_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliostructure',
            name='likes',
        ),
        migrations.AddField(
            model_name='portfoliostructure',
            name='dislike',
            field=models.ManyToManyField(related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='portfoliostructure',
            name='like',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]