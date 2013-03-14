from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^locations/vias/$', 'locations.views.via'),
    url(r'^locations/vias/json$', 'locations.views.vias_json'),
    url(r'^locations/vias/add$', 'locations.views.agregar_via'),
    url(r'^locations/vias/editar/(?P<id_via>\d+)$', 'locations.views.editar_via'),
    url(r'^locations/vias/borrar/(?P<id_via>\d+)$', 'locations.views.eliminar_via'),

    url(r'^locations/usuario/$', 'locations.views.usuario'),
    url(r'^locations/usuarios/json$', 'locations.views.usuarios_json'),

    url(r'^admin/', include(admin.site.urls)),
)
