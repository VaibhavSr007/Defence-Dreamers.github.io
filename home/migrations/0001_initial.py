# Generated by Django 3.2.16 on 2023-02-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('zip', models.CharField(max_length=122)),
                ('desc', models.TextField(default='SOME STRING')),
            ],
        ),
    ]
