# Generated by Django 4.1.1 on 2022-09-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='static/imgs/place'),
        ),
    ]