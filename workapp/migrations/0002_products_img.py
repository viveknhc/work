# Generated by Django 3.2.9 on 2022-02-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]