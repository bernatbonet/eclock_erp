# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


# -------------------------------------------
# APPLICATION NAME
# -------------------------------------------
class Meta:
    verbose_name = _("Localizaciones")
# -------------------------------------------


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
    prefijo = models.CharField(max_length=3, verbose_name=_('Prefijo teléfonico'), help_text=_('Introduzca el prefijo telefónico del país'))
    ue = models.BooleanField(verbose_name=_('Union Europea'), help_text=_('Pertenece a la Union Europea'))
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


# municipio/localidad, provincia/estado, pais pueden ser libres para otros paises
# conviene crear campos libres o obligar a llenarlos


class Direccion(models.Model):
    alias = models.CharField(max_length=60, verbose_name=_('Alias'), help_text=_('Introduzca un alias para la dirección'))
    via = models.ForeignKey('Via', verbose_name=_('Via'), help_text=_('Introduzca la via'))
    direccion1 = models.CharField(max_length=128, verbose_name=_('Dirección 1'), help_text=_('Introduzca la dirección 1'))
    direccion2 = models.CharField(max_length=128, verbose_name=_('Dirección 2'), help_text=_('Introduzca la dirección 1'))
    direccion3 = models.CharField(max_length=128, verbose_name=_('Dirección 3'), help_text=_('Introduzca la dirección 1'))
    numero = models.CharField(max_length=5, verbose_name=_('Número'), help_text=_('Introduzca el número de la dirección'))
    piso = models.CharField(max_length=5, verbose_name=_('Piso'), help_text=_('Introduzca el piso de la dirección'))
    puerta = models.CharField(max_length=5, verbose_name=_('Puerta'), help_text=_('Introduzca el puerta de la dirección'))
    cp = models.CharField(max_length=12, verbose_name=_('Código Postal'), help_text=_('Introduzca el código postal de la dirección'))
    municipio = models.ForeignKey('Municipio', verbose_name=_('Municipio'), help_text=_('Introduzca el municipio de la dirección'))
    provincia = models.ForeignKey('Provincia', verbose_name=_('Provincia'), help_text=_('Introduzca la provincia de la dirección'))
    pais = models.ForeignKey('Pais', verbose_name=_('Pais'), help_text=_('Introduzca el país de la dirección'))

    def _unicode__(self):
        return self.alias

    class Meta:
        verbose_name = _('Dirección')
        verbose_name_plural = _('Direcciones')


class Contactos(models.Model):
    alias = models.CharField(max_length=60, verbose_name=_('Alias'), help_text=_('Introduzca un alias para el contacto'))
    telefono_trabajo = models.CharField(max_length=15, verbose_name=_('Teléfono Trabajo'), help_text=_('Introduzca un teléfono del trabajo para el contacto'))
    telefono_particular = models.CharField(max_length=15, verbose_name=_('Teléfono Particular'), help_text=_('Introduzca un teléfono particular para el contacto'))
    movil_trabajo = models.CharField(max_length=15, verbose_name=_('Móvil Trabajo'), help_text=_('Introduzca un móvil del trabajo para el contacto'))
    movil_particular = models.CharField(max_length=15, verbose_name=_('Móvil Particular'), help_text=_('Introduzca un móvil particular para el contacto'))
    fax_trabajo = models.CharField(max_length=15, verbose_name=_('Fax Trabajo'), help_text=_('Introduzca un fax del trabajo para el contacto'))
    fax_particular = models.CharField(max_length=15, verbose_name=_('Fax Particular'), help_text=_('Introduzca un fax particular para el contacto'))
    email_trabajo = models.CharField(max_length=15, verbose_name=_('Email Trabajo'), help_text=_('Introduzca un email del trabajo para el contacto'))
    email_particular = models.CharField(max_length=15, verbose_name=_('Email Particular'), help_text=_('Introduzca un email particular para el contacto'))

    def __unicode__(self):
        return self.alias

    class Meta:
        verbose_name = _('Contacto')
        verbose_name_plural = _('Contactos')
