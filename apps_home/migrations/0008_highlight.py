# Generated by Django 4.0.4 on 2022-06-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0007_contentsitem_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('img', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
