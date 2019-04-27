from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.


# Administrador
def index(request):
    return render(request, 'templates main/index.html')


# Estudiante
class EstudianteList(ListView):
    model = Estudiante
    template_name = 'list/estudiante_list.html'


class EstudianteCreate(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'create/estudiante_form.html'
    success_url = reverse_lazy('index')


class EstudianteUpdate(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'edit/estudiante_edit.html'
    success_url = reverse_lazy('list_estudiente')


class EstudianteDelete(DeleteView):
    model = Estudiante
    template_name = 'del/estudiante_del.html'
    success_url = reverse_lazy('list_estudiente')


# Plato
class PlatoList(ListView):
    model = Plato
    template_name = 'list/plato_list.html'


class PlatoCreate(CreateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'create/plato_form.html'
    success_url = reverse_lazy('list_plato')


class PlatoUpdate(UpdateView):
    model = Plato
    form_class = PlatoForm
    template_name = 'edit/plato_edit.html'
    success_url = reverse_lazy('list_plato')


class PlatoDelete(DeleteView):
    model = Plato
    template_name = 'del/plato_del.html'
    success_url = reverse_lazy('list_plato')


# Regular
def index_regular(request):
    return render(request, 'templates main/index_regular.html')


class SolicitudPlatoList(ListView):
    model = SolicitudPlato
    template_name = 'list/solicitud_list.html'


class SolicitudPlatoCreate(CreateView):
    model = SolicitudPlato
    template_name = 'create/estudiante_sol.html'
    form_class = SolicitudPlatoForm
    success_url = reverse_lazy('index_regular')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        solicitud = form.save(commit=False)
        plato = Plato.objects.get(id=solicitud.plato_id)
        if form.is_valid() and plato.disp > 0:
            solicitud.save()
            plato.disp = plato.disp - 1
            plato.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class SolicitudPlatoDelete(DeleteView):
    model = SolicitudPlato
    template_name = 'del/solicitud_del.html'
    success_url = reverse_lazy('list_solicitud')


# User
class UserCreate(CreateView):
    model = User
    template_name = 'templates main/login.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
