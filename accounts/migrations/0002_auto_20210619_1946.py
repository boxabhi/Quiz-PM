# Generated by Django 3.2.4 on 2021-06-19 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]