# Generated by Django 4.2.4 on 2023-08-23 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='upload',
            field=models.FileField(upload_to='django_app/static'),
        ),
    ]
