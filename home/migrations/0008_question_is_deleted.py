# Generated by Django 3.2.4 on 2021-06-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210613_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]