# Generated by Django 4.2.4 on 2023-08-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0007_uploads'),
    ]

    operations = [
        migrations.CreateModel(
            name='check_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Tamilnadu', 'Tamilnadu'), ('Karnataka', 'Karnataka')], max_length=30)),
                ('english', models.BooleanField(default=False)),
                ('malayalam', models.BooleanField(default=False)),
                ('hindi', models.BooleanField(default=False)),
            ],
        ),
    ]
