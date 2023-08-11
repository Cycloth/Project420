# Generated by Django 4.2.4 on 2023-08-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('strain_name', models.CharField(max_length=80)),
                ('strain_base', models.CharField(max_length=80)),
                ('strain_id', models.CharField(max_length=80)),
                ('flower_color', models.CharField(max_length=80)),
                ('flower_color2', models.CharField(max_length=80)),
                ('flower_texture', models.CharField(max_length=80)),
                ('flower_density', models.CharField(max_length=80)),
                ('flower_flavor', models.CharField(max_length=80)),
                ('flower_flavor2', models.CharField(max_length=80)),
                ('flower_flavor3', models.CharField(max_length=80)),
                ('flower_effect', models.CharField(max_length=80)),
                ('flower_effect2', models.CharField(max_length=80)),
                ('flower_effect3', models.CharField(max_length=80)),
                ('user_rating', models.CharField(max_length=80)),
                ('user_notes', models.CharField(max_length=80)),
            ],
        ),
    ]