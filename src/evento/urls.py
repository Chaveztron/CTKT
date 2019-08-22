from django.urls import path
from .views import *

urlpatterns = [
    
    path('', comming, name='index2'),
    path('root_jesus/', index, name='index'),
    path('en/', indexen, name='englishp'),
    path('seguimiento/', programa, name='prog'),
    #path('log/', login, name='log'),
    path('registrado/<id>/<nombre>/', satisfatorio, name='registrado' ),
    path('verificado/<id>/<nombre>/', verificar),
    path('tab/', registrados, name='tab'),

    path('reporte_excel/', ReporteUsuarioExcel.as_view(), name='list_users'),

    path('pase/<id>/<nombre>/', GeneratePdf,),

    path('saludos/', HomeView.as_view()),

]