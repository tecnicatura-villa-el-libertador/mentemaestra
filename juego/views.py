
from django.shortcuts import render, redirect
from .forms import IngreseNumero, Registrar
from juego.models import Jugada, Partida, Jugador
from .mastermind import evaluar, crear_numero


def jugar(request, partida_id):
    jugadas = Jugada.objects.filter(partida__id=partida_id).order_by('-id')
    partida = Partida.objects.get(id=partida_id)
    jugadas_ganadoras = []        
    if request.method == 'POST':
        form= IngreseNumero(request.POST)
        #validar=verificar(numero)
        if form.is_valid():
            jugador = partida.turno_de
            apuesta = form.cleaned_data["numero"]
            bien, regular = evaluar(apuesta, jugador.incognita)
            ronda = partida.ronda
            jugada = Jugada.objects.create(jugador=jugador, 
                partida=partida, apuesta=apuesta, bien=bien, 
                regular=regular, ronda=ronda)


            participantes = list(partida.participantes.filter(activo=True))
            print("turno de", partida.turno_de)
            try:
                partida.turno_de = participantes[participantes.index(jugador) + 1]
            except IndexError:
                
                partida.ronda = partida.ronda + 1
                partida.turno_de = participantes[0]
                
            partida.save()

            if bien == 4:
                jugador.activo = False
                jugador.save()

           
            return redirect('jugar', partida_id=partida_id)
    else: 

        jugadas_ganadoras = Jugada.objects.filter(partida=partida, bien=4)

        form= IngreseNumero()
    return render(request, 'comenzar.html', 
        {
        'jugadas':jugadas,
         'form': form,
         'partida': partida,
         'jugadas_ganadoras':jugadas_ganadoras,        
        })

def inicio(request):
    if request.method == 'POST':
        partida = Partida.objects.create()
        return redirect('registro/{}'.format(partida.id))
    return render(request, 'inicio.html', {})    


def registrar(request, partida_id):
    partida = Partida.objects.get(id=partida_id)
    jugadores = partida.participantes.all()
    if request.method == 'POST':

        form= Registrar(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            incognita = crear_numero()
            jugador = Jugador.objects.create(nombre=nombre, 
                incognita=incognita, activo=True)
            if partida.participantes.count() == 0:
                # el primer turno es del primer registrado
                partida.turno_de = jugador
                partida.save() 
            partida.participantes.add(jugador)
            
            if 'comenzar' in request.POST:
                # apretaron el boton verde para comenzar el juego
                return redirect('jugar', partida_id=partida_id)
            return redirect('/registro/{}'.format(partida.id))

    else: 
        form= Registrar()
    return render(request, 'registrar.html', 
        {
        'jugadores':jugadores,
         'form': form,
        })


