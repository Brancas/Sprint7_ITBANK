# Generated by Django 4.1 on 2022-08-12 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0004_delete_empleado_delete_prestamo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(verbose_name='balance')),
                ('iban', models.CharField(max_length=255, verbose_name='iban')),
                ('tipo_cuenta', models.CharField(choices=[('CAP', 'CAJA DE AHORRO EN PESOS'), ('CAD', 'CAJA DE AHORRO EN DOLARES'), ('CC', 'CUENTA CORRIENTE')], max_length=3)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
            ],
        ),
    ]