# Generated by Django 4.2.4 on 2023-08-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=30)),
                ('upload', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]