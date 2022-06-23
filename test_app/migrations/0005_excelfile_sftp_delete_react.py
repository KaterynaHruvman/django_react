# Generated by Django 4.0.5 on 2022-06-23 05:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_react_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['xlsx'])])),
            ],
        ),
        migrations.CreateModel(
            name='Sftp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(default='198.19.243.251', max_length=20)),
                ('port', models.IntegerField(default=2222)),
                ('username', models.CharField(default='tester', max_length=20)),
                ('password', models.CharField(blank=True, default='', max_length=20)),
                ('key', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['', 'pem'])])),
                ('upload_path', models.CharField(default='/inbox/', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='React',
        ),
    ]
