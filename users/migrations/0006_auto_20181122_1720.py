# Generated by Django 2.1.3 on 2018-11-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181122_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='users/pictures'),
        ),
    ]
