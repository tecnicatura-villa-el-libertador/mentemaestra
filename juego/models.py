from django.db import models

# Create your models here.

class Partida(models.Model):

	turno_de=models.CharField(max_length=20)
	ID= models.CharField(max_lenght=10)
	Estado(Registrando, Jugando,Terminado)=models.TextField()

class Jugador(models.Model):
	
	ID=models.IntegerField()
	nombre=models.Charfield(max_lenght=15)
	incognita=models.IntegerField()
	activo=models.BoolField(CheckboxInput)



class Jugada(models.Model):
	
	ronda=models.IntegerField()
	apuesta=models.CharField()
	bien=models.IntegerField()
	regular=models.IntegerField()



	
