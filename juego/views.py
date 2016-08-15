from django.shortcuts import render

def verificar(numero):
    if not numero.isdigit():
        return False
    if len(numero) != 4:
        return False
    if len(set(numero)) != 4:
        return False
    return True

def jugar(request):

	mensaje = "ingresar numero"
	if request.method == 'POST':

		print("POST", request.POST)
		numero=request.POST['numero']
		validar=verificar(numero)
		if validar:
			mensaje="numero valido"
		else:
			mensaje="numero no valido"
	return render(request, 'comenzar.html',
		{'mensaje':mensaje,
		
		})