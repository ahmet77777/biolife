# Generated by Django 4.2.4 on 2023-09-10 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_panel', '0010_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
