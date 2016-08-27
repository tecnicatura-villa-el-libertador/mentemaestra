from django.db import models
from django.db import models

# Create your models here.

class Partida(models.Model):
    ronda = models.PositiveIntegerField(default=1)
    turno_de = models.ForeignKey("Jugador", null=True, blank=True)
    participantes = models.ManyToManyField("Jugador", related_name="partidas")
    privado = models.BooleanField(default =False)
    codigo = models.CharField(max_length=8, null=True)

    estado=models.CharField(max_length=25, default='Registrando',
    	choices=(("Registrando", "Registrando"),("Jugando", "Jugando"), ("Finalizado","Finalizado")))


    def __str__(self):
        return "{} ({})".format(self.turno_de, self.estado)

class Jugador(models.Model):
    
    nombre = models.CharField(max_length=15)
    incognita = models.CharField(max_length=4)
    activo = models.BooleanField()
     

    def __str__(self):
        return "{} ({})".format(self.nombre, self.incognita)

class Jugada(models.Model):
    
    ronda=models.PositiveIntegerField()
    apuesta=models.CharField(max_length=4)
    bien=models.IntegerField()
    regular=models.IntegerField()
    jugador = models.ForeignKey('Jugador', null=True)
    partida = models.ForeignKey('Partida', null=True)

    def __str__(self):
        return "{} ({}) ".format(self.ronda, self.apuesta)


    

