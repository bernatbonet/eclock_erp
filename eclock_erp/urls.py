from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^usuario/$', 'locations.views.usuario'),
    url(r'^locations/vias/$', 'locations.views.via'),
    url(r'^usuario/add/$', 'locations.views.agregar_usuario'),
    url(r'^via/add$', 'locations.views.agregar_via'),
    url(r'^usuario/borrar/(?P<id_usuario>\d+)$', 'locations.views.eliminar_usuario'),
    url(r'^via/borrar/(?P<id_via>\d+)$', 'locations.views.eliminar_via'),
    url(r'^usuario/editar/(?P<id_usuario>\d+)$', 'locations.views.editar_usuario'),
    url(r'^via/editar/(?P<id_via>\d+)$', 'locations.views.editar_via'),

    url(r'^category-detailed/(?P<id_category>\d+)$', 'locations.views.devolver_categoria', name='category-detailed'),
    url(r'^entry-detailed/(?P<id_entry>\d+)$', 'locations.views.devolver_entrada', name='entry-detailed'),

    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
