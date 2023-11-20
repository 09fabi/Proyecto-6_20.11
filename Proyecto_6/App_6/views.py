from django.shortcuts import render, redirect, get_object_or_404
from App_6.models import Proyecto
from App_6.forms import ProyectoForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def listado(request):
    proye = Proyecto.objects.all()
    data = {'proyec': proye}
    return render(request, 'listado.html', data)


def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado')
    else:
        form = ProyectoForm()

    return render(request, 'form_proyecto.html', {'form': form})

def eliminar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    proyecto.delete()
    return redirect('listado')

def actualizar_proyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('listado')
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'update.html', {'form': form})