# Generated by Django 5.1.4 on 2024-12-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dependencies',
            field=models.ManyToManyField(blank=True, null=True, related_name='dependent_tasks', to='projects.task'),
        ),
    ]
