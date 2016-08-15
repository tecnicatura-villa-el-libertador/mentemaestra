from django.db import models

class Partida(models.Model):

    turno_de=models.ForeignKey("Jugador", null=True, blank=True)
    participantes=models.ManyToManyField("Jugador", related_name="partidas")

    estado=models.CharField(max_length=25, default='Registrando',
    	choices=(("Registrando", "Registrando"),("Jugando", "Jugando"), ("Finalizado","Finalizado")))


    def __str__(self):
        return "{} ({})".format(self.turno_de, self.estado)

class Jugador(models.Model):
    
    nombre=models.CharField(max_length=15)
    incognita=models.PositiveIntegerField()
    activo=models.BooleanField()

    def __str__(self):
        return "{} ({})".format(self.nombre, self.incognita)

class Jugada(models.Model):
    
    ronda=models.IntegerField()
    apuesta=models.CharField(max_length=30)
    bien=models.IntegerField()
    regular=models.IntegerField()


    def __str__(self):
        return "{} ({}) ".format(self.ronda, self.apuesta)