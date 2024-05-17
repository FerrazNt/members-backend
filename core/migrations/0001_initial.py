# Generated by Django 5.0.6 on 2024-05-14 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('addres', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='members_profile')),
            ],
        ),
    ]
