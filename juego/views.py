from django.shortcuts import render

# Create your views here.
def comenzar(request):
	mensaje = "ingresar numero"
	return render(request, 'comenzar.html',
		{'mensaje':mensaje,
		})