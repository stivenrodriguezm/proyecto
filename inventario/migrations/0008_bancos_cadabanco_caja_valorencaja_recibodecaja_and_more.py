# Generated by Django 4.1.3 on 2022-12-16 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_alter_pedidos_enviada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bancos',
            fields=[
                ('id_movimiento', models.BigAutoField(primary_key=True, serialize=False)),
                ('banco', models.CharField(max_length=100, null=True, verbose_name='banco')),
                ('concepto', models.CharField(max_length=500, null=True, verbose_name='concepto')),
                ('fecha', models.CharField(max_length=50, null=True, verbose_name='fecha')),
                ('tipo', models.CharField(max_length=50, null=True, verbose_name='tipo')),
                ('valor', models.BigIntegerField(null=True, verbose_name='valor')),
            ],
        ),
        migrations.CreateModel(
            name='CadaBanco',
            fields=[
                ('id_auto', models.BigAutoField(primary_key=True, serialize=False)),
                ('total_bancos', models.BigIntegerField(default=0, null=True, verbose_name='total_bancos')),
                ('bancolombia_lottus', models.BigIntegerField(default=0, null=True, verbose_name='bancolombia_lottus')),
                ('bancolombia_stiven', models.BigIntegerField(default=0, null=True, verbose_name='bancolombia_stiven')),
                ('davivienda', models.BigIntegerField(default=0, null=True, verbose_name='davivienda')),
                ('nequi', models.BigIntegerField(default=0, null=True, verbose_name='nequi')),
                ('daviplata', models.BigIntegerField(default=0, null=True, verbose_name='daviplata')),
            ],
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id_movimiento', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=50, null=True, verbose_name='fecha')),
                ('concepto', models.CharField(max_length=500, null=True, verbose_name='concepto')),
                ('tipo', models.CharField(max_length=50, null=True, verbose_name='tipo')),
                ('subtipo', models.CharField(max_length=50, null=True, verbose_name='subtipo')),
                ('valor', models.BigIntegerField(null=True, verbose_name='valor')),
                ('valorCaja', models.BigIntegerField(null=True, verbose_name='valorCaja')),
            ],
        ),
        migrations.CreateModel(
            name='ValorEnCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valorActual', models.BigIntegerField(null=True, verbose_name='valorActual')),
            ],
        ),
        migrations.CreateModel(
            name='ReciboDeCaja',
            fields=[
                ('id_auto', models.BigAutoField(primary_key=True, serialize=False)),
                ('numero_recibo_caja', models.IntegerField(null=True, verbose_name='numero_recibo_caja')),
                ('metodo_pago', models.CharField(max_length=50, null=True, verbose_name='metodo_pago')),
                ('abono_cancelacion', models.CharField(max_length=50, null=True, verbose_name='abono_cancelacion')),
                ('fecha', models.CharField(max_length=50, null=True, verbose_name='fecha')),
                ('valor', models.BigIntegerField(null=True, verbose_name='valor')),
                ('id_movimiento_bancos', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.bancos')),
                ('id_movimiento_caja', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.caja')),
                ('id_venta', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventario.ventas')),
            ],
        ),
        migrations.CreateModel(
            name='ComprobantesDeEgreso',
            fields=[
                ('id_auto', models.BigAutoField(primary_key=True, serialize=False)),
                ('numero_comprobante_egreso', models.IntegerField(null=True, verbose_name='numero_comprobante_egreso')),
                ('fecha', models.CharField(max_length=50, null=True, verbose_name='fecha')),
                ('metodo_pago', models.CharField(max_length=50, null=True, verbose_name='metodo_pago')),
                ('valor', models.BigIntegerField(null=True, verbose_name='valor')),
                ('facturas', models.CharField(max_length=500, null=True, verbose_name='facturas')),
                ('id_movimiento_bancos', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.bancos')),
                ('id_movimiento_caja', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.caja')),
                ('id_proveedor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventario.proveedores')),
            ],
        ),
    ]
