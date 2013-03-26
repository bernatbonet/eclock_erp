# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


# -------------------------------------------
# APPLICATION NAME
# -------------------------------------------
class Meta:
    verbose_name = _("Productos")


class Idioma(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo del idioma'))
    desc = models.CharField(max_length=60, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion del idioma'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Idioma')
        verbose_name_plural = _('Idiomas')


class TablaNombre(models.Model):
    tabla = models.CharField(max_length=5, verbose_name=_('Tabla'), help_text=_('Introduzca el codigo la tabla'))
    valor = models.CharField(max_length=60, verbose_name=_('Nombre'), help_text=_('Introduzca el nombre de la tabla')) 


class TablaNombreIdioma(models.Model):
    tablanombre = models.ForeignKey('TablaNombre', verbose_name=_('Tabla Nombre'), help_text=_('Introduzca la tabla nombre para este idioma'))

class Tabla1(models.Model) :
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo la tabla 1'))
    desc = models.CharField(max_length=60, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la tabla 1'))

# ------------------------------------------------
# MEASURE MODELS (Controlar paquetes con unidades)
# ------------------------------------------------
class Tallaje(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo del tallaje'))
    desc = models.CharField(max_length=60, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion del tallaje'))

    def __unicode__(self):
        return self.desc

    def cod_tallaje(self):
        return self.cod

    class Meta:
        verbose_name = _('Tallaje')
        verbose_name_plural = _('Tallajes')


class Talla(models.Model):
    tallaje = models.ForeignKey('Tallaje', verbose_name=_('Tallaje'), help_text=_('Introduzca el tallaje'))
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo de la talla'))
    desc = models.CharField(max_length=60, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la talla'))
    pos = models.IntegerField(verbose_name=_('Posicion'), help_text=_('Introduzca la posicion de la talla'))
    unidades = models.IntegerField(default=0, verbose_name=_('Unidades'), help_text=_('Introduzca las unidades que contiene de la talla'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Talla')
        verbose_name_plural = _('Tallas')


# -------------------------------------------
# CLASIFICATION MODELS
# -------------------------------------------
class Temporada(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo de la temporada'))
    desc = models.CharField(max_length=30, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la temporada'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Temporada')
        verbose_name_plural = _('Temporadas')


class Color(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo del color'))
    desc = models.CharField(max_length=30, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion del color'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colores')


class Tipo(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo del tipo'))
    desc = models.CharField(max_length=30, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion del tipo'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Tipo')
        verbose_name_plural = _('Tipos')


class Gama(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo de la gama'))
    desc = models.CharField(max_length=30, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la gama'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Gama')
        verbose_name_plural = _('Gamas')


class Marca(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo de la marca'))
    desc = models.CharField(max_length=30, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la marca'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Marca')
        verbose_name_plural = _('Marcas')


class Familia(models.Model):
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo de la familia'))
    desc = models.CharField(max_length=30, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la familia'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Familia')
        verbose_name_plural = _('Familias')


class Subfamilia(models.Model):
    familia = models.ForeignKey('Familia', verbose_name=_('Familia'), help_text=_('Introduzca la familia'))
    cod = models.CharField(max_length=5, verbose_name=_('Codigo'), help_text=_('Introduzca el codigo de la subfamilia'))
    desc = models.CharField(max_length=30, verbose_name=_('Descripcion'), help_text=_('Introduzca la descripcion de la subfamilia'))

    def __unicode__(self):
        return self.desc

    class Meta:
        verbose_name = _('Subfamilia')
        verbose_name_plural = _('Subfamilias')
