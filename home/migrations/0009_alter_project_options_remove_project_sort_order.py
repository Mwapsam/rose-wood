# Generated by Django 5.0.4 on 2024-04-14 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_project_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RemoveField(
            model_name='project',
            name='sort_order',
        ),
    ]
