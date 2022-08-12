# Generated by Django 4.1 on 2022-08-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=255, verbose_name='Tipo')),
                ('Fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('Total', models.IntegerField(verbose_name='Total')),
            ],
        ),
    ]
