# Generated by Django 3.1 on 2020-08-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200821_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/files'),
        ),
    ]
