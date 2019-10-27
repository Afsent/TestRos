# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bt(models.Model):
    id_bt = models.IntegerField(db_column='ID_bt', primary_key=True, verbose_name='ID ТО')
    name = models.CharField(db_column='Name', max_length=20, verbose_name='ТО')

    class Meta:
        managed = False
        db_table = 'BT'
        verbose_name = 'ТО'
        verbose_name_plural = 'ТО'

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Cities(models.Model):
    id_city = models.IntegerField(db_column='ID_city', primary_key=True)
    id_bt = models.ForeignKey(Bt, models.DO_NOTHING, db_column='ID_bt', verbose_name='ID ТО')
    city = models.CharField(db_column='City', max_length=20, verbose_name='Город')

    class Meta:
        managed = False
        db_table = 'Cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.city


class Groupindicators(models.Model):
    id_group = models.IntegerField(db_column='ID_group', primary_key=True, verbose_name='ID Группы')
    name = models.CharField(db_column='Name', max_length=30, verbose_name='Группа показателей')

    class Meta:
        managed = False
        db_table = 'GroupIndicators'
        verbose_name = 'Группа показателей'
        verbose_name_plural = 'Группы показателей'

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Indicators(models.Model):
    id_indicator = models.IntegerField(db_column='ID_indicator', primary_key=True, verbose_name='ID Показателя')
    id_group = models.ForeignKey(Groupindicators, models.DO_NOTHING, db_column='ID_group', verbose_name='Группа показателей')
    indicator = models.CharField(db_column='Indicator', max_length=30, verbose_name='Показатель')

    class Meta:
        managed = False
        db_table = 'Indicators'
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.indicator.__str__()


class Offices(models.Model):
    id_office = models.IntegerField(db_column='ID_office', primary_key=True)
    id_city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='ID_city', verbose_name='Город')
    office = models.IntegerField(db_column='Office', verbose_name='Офис')

    class Meta:
        managed = False
        db_table = 'Offices'
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.office.__str__()


class Valuebase(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    id_bt = models.ForeignKey(Bt, models.DO_NOTHING, db_column='ID_bt', verbose_name='ТО')
    id_city = models.ForeignKey(Cities, models.DO_NOTHING, db_column='ID_city', verbose_name='Город')
    id_office = models.ForeignKey(Offices, models.DO_NOTHING, db_column='ID_office', verbose_name='Офис')
    id_group = models.ForeignKey(Groupindicators, models.DO_NOTHING, db_column='ID_group', verbose_name='Группа показателей')
    id_indicator = models.ForeignKey(Indicators, models.DO_NOTHING, db_column='ID_indicator', verbose_name='Показатель')
    date = models.DateField(db_column='Date', verbose_name='Дата')
    value = models.IntegerField(db_column='Value', verbose_name='Значение')

    class Meta:
        managed = False
        db_table = 'ValueBase'
        verbose_name = 'Значение'
        verbose_name_plural = 'Значения'

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.value.__str__()

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
