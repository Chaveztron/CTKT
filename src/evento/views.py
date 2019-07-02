from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from openpyxl import Workbook
from django.http.response import HttpResponse
from django.views.generic import TemplateView
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

class ReporteUsuarioExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.order_by('-horaRegistro')
        wb = Workbook()
        ws = wb.active
        ws['B1'] = 'Lista de asistencia'

        ws.merge_cells('B1:E1')

        ws['A3'] = 'ID'
        ws['B3'] = 'Nombres'
        ws['C3'] = 'Puestos'
        ws['D3'] = 'Empresas'
        ws['E3'] = 'Email'
        ws['F3'] = 'Telefonos'
        ws['G3'] = 'Intereses'
        ws['H3'] = 'Participacion'
        ws['I3'] = 'Mensajes'
        ws['J3'] = 'Hora de registro'

        cont = 4

        for usuario in usuarios:
            ws.cell(row = cont, column = 1).value = usuario.id
            ws.cell(row = cont, column = 2).value = usuario.nombre
            ws.cell(row = cont, column = 3).value = usuario.puesto
            ws.cell(row = cont, column = 4).value = usuario.empresa
            ws.cell(row = cont, column = 5).value = usuario.email
            ws.cell(row = cont, column = 6).value = usuario.telefono

            intereses = ""
            for int in usuario.intereses.all():
                intereses = str(int) +", "+intereses

            ws.cell(row = cont, column = 7).value = intereses

            ws.cell(row = cont, column = 8).value = usuario.participaciones.tipo_parti
            ws.cell(row = cont, column = 9).value = usuario.mensaje
            ws.cell(row = cont, column = 10).value = usuario.horaRegistro
            cont+=1

        nombre_archivo = "ReporteUsuariosRegistrados.xlsx"
        response = HttpResponse(content_type="application/ms-excel")
        content = "attachment; filename = {0}".format(nombre_archivo)
        response['Content-Disposition'] = content
        wb.save(response)
        return response


