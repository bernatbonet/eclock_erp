# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


class Meta:
    verbose_name = _("Localizaciones")


class Via(models.Model):
    cod = models.CharField(max_length=2, verbose_name=_('codigo'), help_text=_('Introduzca el codigo de via'), unique=True)
    desc = models.CharField(max_length=35, verbose_name=_('descripcion'), help_text=_('Introduzca la descripcion de la via'), unique=True)

    def __unicode__(self):
        return u'%s %s' % (self.cod, self.desc)

    class Meta:
        verbose_name = _('Via')
        verbose_name_plural = _('Vias')


class Pais(models.Model):
    cod = models.CharField(max_length=2, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo del pais'), unique=True)
    codiso = models.CharField(max_length=3, verbose_name=_('Codigo ISO'), help_text=_('Introduzca el codigo ISO'), unique=True)
    ue = models.BooleanField(verbose_name=_('Union Europea'), help_text=_('Pertenecea la Union Europea'))
    desc = models.CharField(max_length=60, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion del pais'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Pais')
        verbose_name_plural = _('Paises')


class Provincia(models.Model):
    cod = models.CharField(max_length=2, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo de la provincia'), unique=True)
    desc = models.CharField(max_length=60, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la provincia'))
    pais = models.ForeignKey('Pais', verbose_name=_('Pais'), help_text=_('Introduzca el pais'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Provincia')
        verbose_name_plural = _('Provincias')


class Municipio(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo del municipio'))
    desc = models.CharField(max_length=60, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion del municipio'))
    provincia = models.ForeignKey('Provincia', verbose_name=_('Provincia'), help_text=_('Introduzca la provincia'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Municipio')
        verbose_name_plural = _('Municipios')


class Datos(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Entry(models.Model):
    category = models.ForeignKey('Category')
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s, %s' % (self.category.name, self.name)

    def category_desc(self):
        return self.category.name

        class Meta:
            verbose_name = _('Category')
            verbose_name_plural = _('Categories')

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
