import os
import random
from random import sample


Q = {1: ['¿De qué color son las ‘cajas negras’ de los aviones?'],
    2: ['Si en una pecera hay 12 peces y 5 de ellos se ahogan, ¿cuántos peces quedan?'],
    3: ['¿Qué pasó ayer en París de 6 a 7?'],
    4: ['Si un bebé nace en Colombia, pero a los dos años se va a Ecuador, ¿dónde le crecen los dientes?'],
    5: ['Estás corriendo en una carrera y adelantas a la persona que está en segundo lugar, ¿en qué posición pasas a estar?'],
    6: ['La palabra París comienza con “P” y termina con “T”, ¿cierto o falso?'],
    7: ['La palabra París comienza con “P” y termina con “T”, ¿cierto o falso?'],
    8: ['¿Cuál es la pregunta que nadie puede contestar de manera afirmativa?'],
    9: ['¿En qué mes celebran los rusos la Revolución de Octubre?'],
    10: ['Un padre y un hijo van por la carretera, hasta que su auto se estrella en un accidente. El padre muere y el hijo es llevado al hospital para ser operado. Es una operación complicada, por lo que llaman a una eminencia médica de la cirugía para operarlo. Cuando entra en el quirófano dice: “No puedo operarlo, es mi hijo”. ¿Por qué ocurre esto?'],
    11: ['A es el padre de B. Pero B no es el hijo de A. ¿Cómo es posible?'],
    12: ['¿Qué va hacia arriba y hacia abajo, pero sigue estando en el mismo lugar?'],
    13: ['¿Qué palabra usarías para describir a un hombre que no tiene todos los dedos en una mano?'],
    14: ['¿De qué están hechos los pinceles de pelo de camello?'],
    15: ['¿Cuántos son los meses del año que tienen 28 días?'],
    16: ['¿En qué país se fabrican los sombreros Panamá?'],
    17: ['¿Qué animal da nombre a las Islas Canarias?'],
    18: ['Un conductor de camión está bajando por una calle en sentido contrario, y por el camino se cruza por lo menos con diez policías. ¿Por qué no lo detienen?'],
    19: ['¿Por qué un hombre de cuarenta y dos años de edad tan solo ha podido celebrar diez cumpleaños?'],
    20: ['Antes de que el Monte Everest fuera descubierto, ¿cuál era la montaña más alta del mundo?']}

A = {1: ['naranja', 'negra', 'blanca', 'esa joda ni existe'],
     2: ['5', '7', '12', '0'],
     3: ['un incendio', 'una hora', 'una tarea', 'nada'],
     4: ['Colombia', 'Ecuador', 'En la frontera', 'ninguna de las anteriores'],
     5: ['primero', 'segundo', 'tercero', 'no se puede'],
     6: ['cierto', 'falso', 'no se puede', 'no lo se'],
     7: ['sur', 'norte', 'oriente', 'ninguna de las anteriores'],
     8: ['Donde estas?', 'Donde vas?', 'Estas Dormido', 'Que dia es hoy'],
     9: ['Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
     10: ['Es la madre', 'Es el padre', 'el niño ya esta muerto', 'no lo cubre el seguro :v'],
     11: ['si', 'no', 'tal vez', 'no lo se'],
     12: ['el cielo', 'una aguja', 'la escalera', 'un anillo'],
     13: ['No se puede', 'igual que todos', 'Por el nombre', 'Papi, de que me habla?'],
     14: ['De pelos de camello', 'No existen', 'Pelo de ardilla', 'Estan descontinuados'],
     15: ['1', '12', '2', '0'],
     16: ['Panama', 'Ecuador', 'Bolivia', 'Colombia'],
     17: ['El canario', 'El Perro', 'El gato <3', 'El zorro'],
     18: ['No es posible', 'Maneja una ambulacia', 'Va a pie', 'dimension alterna'],
     19: ['Nacio en un año bisiesto', 'Detuvo el tiempo', 'viajo en el tiempo', 'Ya esta muerto'],
     20: ['Monte Everest', 'Kanchenjunga', 'Makalu', 'K2']}

opciones = ['a', 'b', 'c', 'd']

def crear():
    os.makedirs('C:\Quices')
    os.chdir('C:\Quices')
    os.path.abspath('.')

def abrir(nombre, tipo):
    return open(nombre,tipo)

def aleatorio(inicio, fin, tamanio):
    #print(sample([x for x in range(inicio, fin)], limite))
    #print ('')
    #print ('')
    return sample([x for x in range(inicio, fin)], tamanio)

def escribir(doc,cadena):
    doc.write(cadena)
    doc.write('\n')

crear()
for i in range(35):
    quiz = abrir('Q('+str(i+1) + ').txt', 'w')
    Preguntas = aleatorio(1, 21, 20)
    print(Preguntas)
    for j in range(20):
        print(j)
        Respuesta = aleatorio(0, 4, 4)
        escribir(quiz, str(j+1) + '.' + Q[Preguntas[j]][0])
        for k in range(4):
            #print (k)
            #print (str(opciones[k]) + '.' + str(A[Preguntas[j]][Respuestas[k]]) + '\n')
            escribir(quiz, opciones[k] + '.' +A[Preguntas[j]][Respuesta[k]] + '\n')
        quiz.write('\n')
    quiz.close()