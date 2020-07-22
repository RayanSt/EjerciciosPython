# Brayan Parra - 20171020156
# -*- coding: 850 -*-
import smtplib
import json, requests
print('Que bonito es saludar y ser saludado')
print(' ')

info = {'name': '','country': '','temp': '','feels_like':'','temp_min':'',"temp_max":'','pressure':'','humidity':''}
url = 'http://api.openweathermap.org/data/2.5/weather?q=Bogot ,CO&APPID=a8f1a8f6c22965ea367b6f1d3e6fa69a'
response = requests.get(url)
response.raise_for_status()

print(response)
diccionario = response.json()
print(diccionario)
print(' ')
JuegoEnMarcha = True
i = 1
print(diccionario['name'],diccionario['sys']['country'])
info['name'] = diccionario['name']
info['country'] = diccionario['sys']['country']
#print(diccionario['sys']['country'])
for key in diccionario['main']:
    info['temp'] = diccionario['main']['temp']
    info['feels_like'] = diccionario['main']['feels_like']
    info['temp_min'] = diccionario['main']['temp_min']
    info['temp_max'] = diccionario['main']['temp_max']
    info['pressure'] = diccionario['main']['pressure']
    info['humidity'] = diccionario['main']['humidity']

def mandar(cadena):
    objetoSmt= smtplib.SMTP('smtp.gmail.com',587)
    type(objetoSmt)
    objetoSmt.ehlo()

    objetoSmt.starttls()

    objetoSmt.login(' prueba.python2019@gmail.com ',' noesnadasegura ')

    objetoSmt.sendmail(' prueba.python2019@gmail.com ',' bsparrap@gmail.com ', cadena)

    objetoSmt.quit()

#cadena = json.dumps(info)
cadena = ''
for key in info:
    if key == 'name' or key == 'country':
        if info[key] == 'Bogot ':
            cadena = cadena + 'Bogota, '
        else:
            cadena = cadena + str(info[key]) + '\n'
    if key != 'name' and key != 'country' and key != 'temp' and key != 'humidity':
        cadena = cadena + str(key) + ': ' + str(info[key]) + '\n'
    if key == 'temp':
        if info[key] <= 273.15:
            cadena = cadena + str(key) + ': ' + str(info[key]) + '. Muy frio, abrigate bien' + '\n'
        if info[key] > 273.15 and info[key] <= 283.15:
            cadena = cadena + str(key) + ": " + str(info[key])+ ". frio, abrigate un poco" + "\n"
        if info[key] > 283.15 and info[key] <= 293.15:
            cadena = cadena + str(key) + ": " + str(info[key]) + ". Templado, no es necesario abrigo" + "\n"
        if info[key] > 293.15 and info[key] <= 298.15:
            cadena = cadena + str(key) + ": " + str(info[key]) + ". Calido, esta freco, usa ropa comoda" + "\n"
        if info[key] > 298.15 and info[key] <= 298.15:
            cadena = cadena + str(key) + ": " + str(info[key]) + ". Papi, vos estas es en la costa :v" + "\n"

    if key == 'humidity':
        if info[key] < 50:
            cadena = cadena + str(key) + ": " + str(info[key]) + ". permance tranquilo, no llovera" + "\n"
        else:
            cadena = cadena + str(key) + ': ' + str(info[key]) + '. Yo de vos llevaba sombrilla' + '\n'
    #print(key, ' : ', info[key])
    #cadena += str(key)+ ': '+ str(info[key])
    #cadena += key

print(' ')
print(cadena)
mandar(cadena)