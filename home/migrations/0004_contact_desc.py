# Generated by Django 3.2.16 on 2023-03-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230304_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default='SOME STRING'),
        ),
    ]