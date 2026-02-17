from django.shortcuts import render, redirect, get_object_or_404
from .models import Moto
from .forms import MotoForm


def llista_motos(request):
    motos = Moto.objects.all()
    return render(request, 'motos/llista.html', {'motos': motos})


def crear_moto(request):
    if request.method == 'POST':
        form = MotoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('llista_motos')
    else:
        form = MotoForm()
    return render(request, 'motos/form.html', {'form': form})


def editar_moto(request, id):
    moto = get_object_or_404(Moto, id=id)
    if request.method == 'POST':
        form = MotoForm(request.POST, instance=moto)
        if form.is_valid():
            form.save()
            return redirect('llista_motos')
    else:
        form = MotoForm(instance=moto)
    return render(request, 'motos/form.html', {'form': form})


def eliminar_moto(request, id):
    moto = get_object_or_404(Moto, id=id)
    moto.delete()
    return redirect('llista_motos')

