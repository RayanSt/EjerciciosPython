import random

'''Crear variables'''

print('Juego: Piedra, Papel, Tijera, Lagarto, Spock')
print('Que decide escoger: ')
opcionJugador = input()

'''La maquina escoge una opción con la función random, para ver mas documentación sobre random https://docs.python.org/3.7/library/random.html'''

maquina = random.randint(1,5)

if maquina == 1:
    opcionMaquina = 'Piedra'
elif maquina == 2:
    opcionMaquina = 'Papel'
elif maquina == 3:
    opcionMaquina = 'Tijera'
elif maquina == 4:
    opcionMaquina = 'Lagarto'
elif maquina == 5:
    opcionMaquina = 'Spock'

'''De aca en adelante pueden colocar las validaciones para el juego'''

if opcionJugador == 'Piedra':
    jugador = 1
elif opcionJugador == 'Papel':
    jugador = 2
elif opcionJugador == 'Tijera':
    jugador = 3
elif opcionJugador == 'Lagarto':
    jugador = 4
elif opcionJugador == 'Spock':
    jugador = 5

#opcion1
if maquina == 1 and jugador==3:
    print('gano la maquina')
elif maquina == 1 and jugador==4:
    print('gano la maquina')
elif maquina == 1 and jugador==2:
    print('gano el jugador')
elif maquina == 1 and jugador==5:
    print('gano el jugador')
elif maquina == 1 and jugador==1:
    print('Empate')

#opcion2
if maquina == 2 and jugador==1:
    print('gano la maquina')
elif maquina == 2 and jugador==5:
    print('gano la maquina')
elif maquina == 2 and jugador==3:
    print('gano el jugador')
elif maquina == 2 and jugador==4:
    print('gano el jugador')
elif maquina == 2 and jugador==2:
    print('Empate')

#opcion3
if maquina == 3 and jugador==2:
    print('gano la maquina')
elif maquina == 3 and jugador==4:
    print('gano la maquina')
elif maquina == 3 and jugador==5:
    print('gano el jugador')
elif maquina == 3 and jugador==1:
    print('gano el jugador')
elif maquina == 3 and jugador==3:
    print('Empate')

#opcion4
if maquina == 4 and jugador==2:
    print('gano la maquina')
elif maquina == 4 and jugador==5:
    print('gano la maquina')
elif maquina == 4 and jugador==1:
    print('gano el jugador')
elif maquina == 4 and jugador==3:
    print('gano el jugador')
elif maquina == 4 and jugador==4:
    print('Empate')

#opcion5
if maquina == 5 and jugador==1:
    print('gano la maquina')
elif maquina == 5 and jugador== 3:
    print('gano la maquina')
elif maquina == 5 and jugador==2:
    print('gano el jugador')
elif maquina == 5 and jugador==4:
    print('gano el jugador')
elif maquina == 5 and jugador== 5:
    print('Empate')


print('seleccion de la maquina', opcionMaquina)
print('seleccion del jugador', opcionJugador)
print('Gracias por jugar')