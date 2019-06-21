from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    form = RegistrerForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, f'Registro exitoso')
            return redirect('/')
    else:
        form = RegistrerForm()

    context = {
        'form':form
    }

    return render(request, 'evento/index.html', context)

def registrados(request):
    registrados = Usuario.objects.order_by('-horaRegistro')
    context = {
        'usuarios': registrados,
    }
    return render(request, 'evento/tabulado.html', context)