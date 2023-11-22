# Generated by Django 4.2.4 on 2023-08-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0006_rename_fileupload_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audioname', models.CharField(max_length=30)),
                ('audioupload', models.FileField(upload_to='django_app/static')),
                ('videoname', models.CharField(max_length=30)),
                ('videoupload', models.FileField(upload_to='django_app/static')),
                ('pdfname', models.CharField(max_length=30)),
                ('pdfupload', models.FileField(upload_to='django_app/static')),
            ],
        ),
    ]
