# Generated by Django 4.0.4 on 2022-06-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('statement', models.CharField(max_length=100)),
                ('style', models.CharField(max_length=100)),
            ],
        ),
    ]
