# Generated by Django 4.1.6 on 2023-03-04 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebPortfolioApp', '0008_alter_portfoliostructure_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliostructure',
            name='likes',
        ),
        migrations.AddField(
            model_name='portfoliostructure',
            name='liked',
            field=models.ManyToManyField(blank=True, default=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebPortfolioApp.portfoliostructure')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
