from django import forms
from .models import *
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import ModelChoiceField

class RegistrerForm(forms.ModelForm):
    nombre = forms.CharField(required=True, label='',
                            widget=forms.TextInput(
                                attrs={
                                    "placeholder": "Nombre",
                                    'class' :"form-control wow fadeInUp",
                                    'data-wow-delay' :"100ms"
                                }))
    puesto = forms.CharField(required=True, label='',
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "Puesto",
                                     'class': "form-control wow fadeInUp",
                                     'data-wow-delay': "100ms"
                                 }))
    empresa = forms.CharField(required=True, label='',
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "Empresa",
                                     'class': "form-control wow fadeInUp",
                                     'data-wow-delay': "100ms"
                                 }))
    email = forms.EmailField(required=True, label='',
                             widget=forms.TextInput(
                                 attrs={
                                     "placeholder": "Email",
                                     'class': "form-control wow fadeInUp",
                                     'data-wow-delay': "100ms"
                                 }))
    telefono = forms.CharField(required=True, label='',
                              widget=forms.TextInput(
                                  attrs={
                                      "type": "tel",
                                      "pattern": "[0-9]{3}[0-9]{3}[0-9]{4}",
                                      "placeholder": "Telefono",
                                      'class': "form-control wow fadeInUp",
                                      'data-wow-delay': "100ms"
                                  }))
    intereses = forms.ModelMultipleChoiceField(label='Interesado en:',
                                               queryset=Interes.objects.all(),
                                               widget=forms.CheckboxSelectMultiple
                                                   (attrs={

                                               }), required=True)
    """""
    participacion = forms.ModelMultipleChoiceField(label='Interesado en:',
                                               queryset=Tipo_participacion.objects.all(),
                                               widget=forms.RadioSelect
                                                   (attrs={

                                               }), required=True)
    """
    participaciones = forms.ModelChoiceField(label='Interesado en participar como: ', queryset=Tipo_participacion.objects.all(), initial=0)

    mensaje = forms.CharField(required=False, label='',
                              widget=forms.TextInput(
                                  attrs={
                                      "placeholder": "Escriba algun mensaje o pregunta",
                                      'class': "form-control wow fadeInUp",
                                      'data-wow-delay': "100ms"
                                  }))



    class Meta:
        model = Usuario
        fields = ('nombre', 'puesto', 'empresa', 'email',
                  'telefono','intereses','participaciones','mensaje',)