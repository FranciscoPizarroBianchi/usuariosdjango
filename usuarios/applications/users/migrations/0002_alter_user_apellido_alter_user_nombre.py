# Generated by Django 4.0.3 on 2022-03-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellido',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombre',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]