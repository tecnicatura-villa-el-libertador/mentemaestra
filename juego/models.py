from django.db import models

# Create your models here.

class Partida(models.Model):

        turno_de=models.ForeignKey(Jugador)
        participantes=models.ManytoManyField("participante", related_nombre="partidas")
    
        estado=models.Charfield(max_length=25, choices=(("Registrando", "Registrando")("Jugando", "Jugando"), ("Finalizado","Finalizado")))
    

        def __str__(self):
            return "{} ({})".format(self.turno_de, self.estado)

class Jugador(models.Model):
    
        ID=models.IntegerField()
        nombre=models.Charfield(max_lenght=15)
        incognita=models.PositiveIntegerField()
        activo=models.BoolField(CheckboxInput)

        def __str__(self):
            return "{} ({})".format(self.nombre, self.incognita)

class Jugada(models.Model):
    
        ronda=models.IntegerField()
        apuesta=models.CharField()
        bien=models.IntegerField()
        regular=models.IntegerField()
    

        def __str__(self):
            return "{} ({})".format(self.ronda, self.apuesta self.bien self.regular)


    
