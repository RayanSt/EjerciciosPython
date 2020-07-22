# Tic Tac Toe
# Esta basado casi en su totalidad en el libro Making Games with Python & Pygame
# escrito por Al Sweigart, trate de adaptarlo, pero el ya tenia el algoritmo para jugar con  la maquina

import random


def imprimirTablero(tableroJuego):
    print(' ' + tableroJuego[7] + ' | ' + tableroJuego[8] + ' | ' + tableroJuego[9])
    print('-----------')
    print(' ' + tableroJuego[4] + ' | ' + tableroJuego[5] + ' | ' + tableroJuego[6])
    print('-----------')
    print(' ' + tableroJuego[1] + ' | ' + tableroJuego[2] + ' | ' + tableroJuego[3])


def Letras():
        return ['X', 'O']


def TurnoInicial():
    # un random para seleccionar quien comienza jugando
    if random.randint(0, 1) == 1:
        return 'Maquina'
    else:
        return 'Juagador'


def JugarOtraVez():
    print('Jugar de nuevo? (si/no)')
    return input().lower().startswith('s')


def Mover(tableroJuego, letter, move):
    tableroJuego[move] = letter


def Ganador(Tablero, Letra):
    return ((Tablero[7] == Letra and Tablero[8] == Letra and Tablero[9] == Letra) or (Tablero[4] == Letra and Tablero[5] == Letra and Tablero[6] == Letra) or
            (Tablero[1] == Letra and Tablero[2] == Letra and Tablero[3] == Letra) or  # columnas
            (Tablero[7] == Letra and Tablero[4] == Letra and Tablero[1] == Letra) or (Tablero[8] == Letra and Tablero[5] == Letra and Tablero[2] == Letra) or
            (Tablero[9] == Letra and Tablero[6] == Letra and Tablero[3] == Letra) or  # diagonales
            (Tablero[7] == Letra and Tablero[5] == Letra and Tablero[3] == Letra) or (Tablero[9] == Letra and Tablero[5] == Letra and Tablero[1] == Letra))


def CopiaDeTablero(tableroJuego):
    # se crea una copia del tablero
    Duplicado = []
    for i in tableroJuego:
        Duplicado.append(i)

    return Duplicado


def EspacioVacio(tableroJuego, jugada):
    return tableroJuego[jugada] == ' '


def MovimientoJugador(tableroJuego):
    Jugada = ' '
    while Jugada not in '1 2 3 4 5 6 7 8 9'.split() or not EspacioVacio(tableroJuego, int(Jugada)):
        print('Cual sera su movimiento? (1-9)')
        Jugada = input()
    return int(Jugada)


def MovimientoAleatorio(tableroJuego, movesList):
    # Valida los posibles movimientos
    PosibleMoviento = []
    for i in movesList:
        if EspacioVacio(tableroJuego, i):
            PosibleMoviento.append(i)

    if len(PosibleMoviento) != 0:
        return random.choice(PosibleMoviento)
    else:
        return None


def MovimientoMaquina(tableroJuego, LetraComputador):
    if LetraComputador == 'X':
        LetraJugador = 'O'
    else:
        LetraJugador = 'X'

    # Mira si el jugador puede ganar y lo bloquea
    for i in range(1, 10):
        copia = CopiaDeTablero(tableroJuego)
        if EspacioVacio(copia, i):
            Mover(copia, LetraComputador, i)
            if Ganador(copia, LetraComputador):
                return i

    for i in range(1, 10):
        copia = CopiaDeTablero(tableroJuego)
        if EspacioVacio(copia, i):
            Mover(copia, LetraJugador, i)
            if Ganador(copia, LetraJugador):
                return i

    #Mira si las esquinas estan libres para tomarlas
    move = MovimientoAleatorio(tableroJuego, [1, 3, 7, 9])
    if move != None:
        return move

    # Trata de tomar el centro si esta libre
    if EspacioVacio(tableroJuego, 5):
        return 5

    return MovimientoAleatorio(tableroJuego, [2, 4, 6, 8])


def TableroLleno(tableroJuego):
    for i in range(1, 10):
        if EspacioVacio(tableroJuego, i):
            return False
    return True


print('Bienvenidos a  Tic Tac Toe!')
print('Movimientos posibles, tengalos presente')
print('9. arriba a la derecha')
print('8. arriba en el medio')
print('7. arriba a la izquierda')
print('6. en el medio a la derecha')
print('5. en el medio en el centro')
print('4. en el medio a la izquierda')
print('3. abajo a la derecha')
print('2. abajo en el medio')
print('1. abajo a la izquierda')

while True:
    tableroJuego = [' '] * 10
    playerLetter, LetraComputador = Letras()
    Turno = TurnoInicial()
    print(Turno + ' Inicia.')
    JuegoEnMarcha = True

    while JuegoEnMarcha:
        #Jugador
        if Turno == 'Jugador':
            imprimirTablero(tableroJuego)
            movimiento = MovimientoJugador(tableroJuego)
            Mover(tableroJuego, playerLetter, movimiento)

            if Ganador(tableroJuego, playerLetter):
                imprimirTablero(tableroJuego)
                print('Ganaste!')
                JuegoEnMarcha = False
            else:
                if TableroLleno(tableroJuego):
                    imprimirTablero(tableroJuego)
                    print('Empate!')
                    break
                else:
                    Turno = 'Maquina'

        else:
            #Maquina
            movimiento = MovimientoMaquina(tableroJuego, LetraComputador)
            Mover(tableroJuego, LetraComputador, movimiento)

            if Ganador(tableroJuego, LetraComputador):
                imprimirTablero(tableroJuego)
                print('La Maquina lo consiguio! Perdiste.')
                JuegoEnMarcha = False
            else:
                if TableroLleno(tableroJuego):
                    imprimirTablero(tableroJuego)
                    print('Empate!')
                    break
                else:
                    Turno = 'Jugador'

    if not JugarOtraVez():
        break