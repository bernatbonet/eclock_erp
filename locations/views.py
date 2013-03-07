from django.shortcuts import render_to_response
from django.template import RequestContext
from locations.models import Datos, Via, Category, Entry
from locations.forms import UsuariosForm, ViasForm
from django.http import HttpResponseRedirect


def usuario(request):
    usuarios = Datos.objects.all()
    return render_to_response('usuario.html', {'usuarios': usuarios}, context_instance=RequestContext(request))


def via(request):
    vias = Via.objects.all()
    return render_to_response('via.html', {'vias': vias, 'fields': Via._meta.fields}, context_instance=RequestContext(request))


def agregar_usuario(request):
    if request.method == "POST":
        formulario = UsuariosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/usuario/")
    else:
        formulario = UsuariosForm()
    return render_to_response("agregar_usuario.html", {'formulario': formulario}, context_instance=RequestContext(request))


def agregar_via(request):
    if request.method == "POST":
        formulario = ViasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/via/")
    else:
        formulario = ViasForm()

    return render_to_response("agregar_via.html", {'formulario': formulario}, context_instance=RequestContext(request))


def eliminar_usuario(request, id_usuario):
    usuario = Datos.objects.get(pk=id_usuario)
    usuario.delete()
    return HttpResponseRedirect("../")


def eliminar_via(request, id_via):
    usuario = Via.objects.get(pk=id_via)
    usuario.delete()
    return HttpResponseRedirect("../")


def editar_usuario(request, id_usuario):
    usuario = Datos.objects.get(pk=id_usuario)
    if request.method == "POST":
        formulario = UsuariosForm(request.POST, instance=usuario)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect("../")
    else:
        formulario = UsuariosForm(instance=usuario)

    return render_to_response("editar_usuario.html", {'formulario': formulario}, context_instance=RequestContext(request))


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


def devolver_categoria(request, id_category):
    categoria = Category.objects.get(pk=id_category)
    return render_to_response({'category': categoria}, context_instance=RequestContext(request))


def devolver_entrada(request, id_entry):
    entrada = Entry.objects.get(pk=id_entry)
    categoria = entrada.category
    return render_to_response({'category': categoria, 'entry': entrada}, context_instance=RequestContext(request))
