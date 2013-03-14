#from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from locations.models import Datos, Via
from locations.forms import ViasForm


# Usuarios
def usuario(request):
    usuarios = Datos.objects.all()
    return render_to_response('usuario.html', {'usuarios': usuarios}, context_instance=RequestContext(request))


def usuarios_json(request):
    return HttpResponse(Datos.objects.all().values(), mimetype="application/json")


# Vias
def via(request):
    vias = Via.objects.all()
    return render_to_response('via.html', {'vias': vias, 'fields': Via._meta.fields}, context_instance=RequestContext(request))


@csrf_exempt
def vias_json(request):
    data = []
    for item in Via.objects.all():
        data.append({'cod': item.cod,  'desc': item.desc})
    sort = []
    sort.append(['cod', 'asc'])
    result = {'currentPage': 1, 'totalRows': Via.objects.all().count(), 'sort': sort, 'data': data}
    json = simplejson.dumps(result)
    return HttpResponse(json, mimetype="application/json")


def agregar_via(request):
    if request.method == "POST":
        formulario = ViasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/locations/vias/")
    else:
        formulario = ViasForm()

    return render_to_response("agregar_via.html", {'formulario': formulario}, context_instance=RequestContext(request))


def editar_via(request, id_via):
    via = Via.objects.get(pk=id_via)
    if request.method == "POST":
        formulario = ViasForm(request.POST, instance=via)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect("../")
    else:
        formulario = ViasForm(instance=via)

    return render_to_response("editar_via.html", {'formulario': formulario}, context_instance=RequestContext(request))


def eliminar_via(request, id_via):
    usuario = Via.objects.get(pk=id_via)
    usuario.delete()
    return HttpResponseRedirect("../")
