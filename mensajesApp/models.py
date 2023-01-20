from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensajes(models.Model):
    fecha=models.DateField()
    cuerpo=models.CharField(max_length=150)
    emisor=models.CharField(max_length=50)
    receptor=models.ForeignKey(User, on_delete=models.CASCADE )
    leido=models.BooleanField()

    def __str__(self):
        return f"{self.emisor} | {self.receptor} | {self.cuerpo} , {self.fecha} " 

