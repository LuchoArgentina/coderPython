from django import forms
from django.contrib.auth.models import User
from .models import Mensajes





class crearMensajeForm(forms.Form):
    fecha=forms.DateField(label="Fecha")
    cuerpo=forms.CharField(label="Mensaje",max_length=150)

    # receptor=forms.ChoiceField(choices={1:"admin",2:"Maria"} , required=True, label="Receptor")
    receptor=forms.IntegerField()

    class Meta:
        model=Mensajes
        fields=["fecha","cuerpo","receptor"]
        help_texts={k:"" for k in fields}