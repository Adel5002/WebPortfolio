# Generated by Django 4.1.6 on 2023-02-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPortfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliostructure',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]