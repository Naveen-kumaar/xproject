# Generated by Django 5.0.7 on 2024-07-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=10)),
                ('C_Password', models.CharField(max_length=10)),
            ],
        ),
    ]
