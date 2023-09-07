# Generated by Django 4.1.2 on 2022-11-16 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_remove_registration_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('query_desc', models.CharField(max_length=200)),
            ],
        ),
    ]