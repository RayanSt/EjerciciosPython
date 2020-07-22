
# Brayan Parra - 20171020156

import json, requests
print('sistema de Localización conjunta')
print('aquí podra saber si dos personajes estan en la misma localización')
print(' ')

def JugarOtraVez():
    print('Intentar de nuevo? (si/no): ')
    return input().lower().startswith('s')

url = 'https://rickandmortyapi.com/api/character/'
response = requests.get(url)
response.raise_for_status()

#print(response)
diccionario = response.json()
#print(diccionario)
print(' ')
JuegoEnMarcha = True
while JuegoEnMarcha:
    i = 1
    for key in diccionario['results']:
        print(str(i),': ' ,key['name'])
        i+=1
    i=1
    print(' ')
    personaje = int(input('ingrese el numero del persona que desea seleccionar: '))
    comparar = int(input('ingrese el numero del persona que desea comparar: '))
    localizacion1 = ''
    localizacion2 = ''
    for key in diccionario['results']:
        if personaje == i:
            print('personaje: ')
            print(str(i),': ' ,key['name'])
            #print(key)
            localizacion1 = key
            print(' ')
        if comparar == i:
            print('comparar: ')
            print(str(i),': ' ,key['name'])
            #print(key)
            localizacion2 = key
        i+=1
    if localizacion1['location']['name'] == localizacion2['location']['name']:
        print('Enhorabuena ambos personajes estan en la misma Locacion')
        print(localizacion1['location']['name'])
    else:
        print('Mala suerte, los personajes estan en locaciones distintas')
        print(str(personaje),': ' ,localizacion1['name'], ' Locacion: ', localizacion1['location']['name'])
        print(str(comparar), ': ', localizacion2['name'], ' Locacion: ', localizacion2['location']['name'])
    print(' ')
    if input('desea saber los otros datos de los personajes que selccionó? (si/no)?: ').lower().startswith('s'):
        print(str(personaje), ': ', localizacion1['name'])
        print(' Status: ', localizacion1['status'])
        print(' Specie: ', localizacion1['species'])
        print(' Type: ', localizacion1['type'])
        print(' Gender: ', localizacion1['gender'])
        print(' Origin: ', localizacion1['origin']['name'])
        print(' ')
        print(str(comparar), ': ', localizacion2['name'])
        print(' Status: ', localizacion2['status'])
        print(' Specie: ', localizacion2['species'])
        print(' Type: ', localizacion2['type'])
        print(' Gender: ', localizacion2['gender'])
        print(' Origin: ', localizacion2['origin']['name'])



    if not JugarOtraVez():
        break