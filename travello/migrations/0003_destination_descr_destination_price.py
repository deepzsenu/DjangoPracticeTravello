# Generated by Django 4.1.1 on 2022-09-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_alter_destination_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='descr',
            field=models.TextField(default='description'),
        ),
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=700),
        ),
    ]