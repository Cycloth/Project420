# Generated by Django 4.2.4 on 2023-08-12 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project_420", "0002_rename_flower_flavor3_form_flower_aroma_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="form",
            old_name="strain_base",
            new_name="strain_THC",
        ),
    ]
