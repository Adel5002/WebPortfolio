# Generated by Django 4.1.6 on 2023-03-14 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebPortfolioApp', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]