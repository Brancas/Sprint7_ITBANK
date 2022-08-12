# Generated by Django 4.1 on 2022-08-12 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0001_initial'),
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sucursal.sucursal'),
        ),
        migrations.AlterModelTable(
            name='empleado',
            table='empleado',
        ),
    ]
