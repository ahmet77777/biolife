# Generated by Django 4.2.4 on 2023-09-08 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('a_panel', '0003_userpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_pincode', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='changepassword', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]