# Generated by Django 4.2.4 on 2023-09-06 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
