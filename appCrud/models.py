# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Inv(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    unidadfuncional = models.CharField(db_column='UnidadFuncional', max_length=9, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)
    idtanque = models.CharField(db_column='IdTanque', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idproducto = models.CharField(db_column='idProducto', max_length=10, blank=True, null=True)  # Field name made lowercase.
    productoname = models.CharField(db_column='ProductoName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idunidadmedida = models.CharField(db_column='idUnidadMedida', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unidadmedida = models.CharField(db_column='UnidadMedida', max_length=50, blank=True, null=True)  # Field name made lowercase.
    volumeninicial = models.DecimalField(db_column='volumenInicial', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    volumenactual = models.DecimalField(db_column='volumenActual', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    temperatura = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    densidad = models.DecimalField(db_column='Densidad', max_digits=7, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    certificadocalidad = models.CharField(db_column='CertificadoCalidad', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Inv'


