# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
from locations.models import Direccion, Contacto


# -------------------------------------------
# APPLICATION NAME
# -------------------------------------------
class Meta:
    verbose_name = _("Personas")
# -------------------------------------------


class NifCif(models.Model):
    nif = models.CharField(max_length=13, verbose_name=_('Nif'), help_text=_('Introduzca el nif de la persona/empresa'))
    nif_pais = models.CharField(max_length=13, verbose_name=_('Nif Pais'), help_text=_('Introduzca el nif del país de la persona/empresa'))
    nombre = models.CharField(max_length=60, verbose_name=_('Nombre'), help_text=_('Introduzca el nombre de la persona/empresa'))
    apellidos = models.CharField(max_length=60, verbose_name=_('Apellidos'), help_text=_('Introduzca los apellidos de la persona/empresa'))
    fecha_nacimiento = models.DateField(verbose_name=_('Fecha de Nacimiento'), help_text=_('Introduzca la fecha de nacimiento de la persona/empresa'))

    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.apellidos)

    class Meta:
        verbose_name = _('NifCif')
        verbose_name_plural = _('NifCif')


class NifCifDireccion(models.Model):
    alias = models.CharField(max_length=60, verbose_name=_('Alias'), help_text=_('Introduzca un alias para la dirección'))
    nifcif = models.ForeignKey('NifCif', verbose_name=_('Nif'), help_text=_('Introduzca el nif de la dirección'))
    direccion = models.ForeignKey('Direccion', verbose_name=_('Direccion'), help_text=_('Introduzca la dirección'))

    def __unicode__(self):
        return u'%s' % (self.alias)

    class Meta:
        verbose_name = _('Dirección Nif')
        verbose_name_plural = _('Direcciones Nif')


class NifCifContactos(models.Model):
    alias = models.CharField(max_length=60, verbose_name=_('Alias'), help_text=_('Introduzca un alias para el contacto'))
    nifcif = models.ForeignKey('NifCif', verbose_name=_('Nif'), help_text=_('Introduzca el nif del contacto'))
    contacto = models.ForeignKey('Contacto', verbose_name=_('Contacto'), help_text=_('Introduzca el contacto del contacto'))

    def __unicode__(self):
        return u'%s' % (self.alias)

    class Meta:
        verbose_name = _('Contacto Nif')
        verbose_name_plural = _('Contactos Nif')
