from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tab/', registrados, name='tab'),

    path('reporte_excel/', ReporteUsuarioExcel.as_view(), name='list_users'),

    path('pase/<id>/', GeneratePdf,),

]