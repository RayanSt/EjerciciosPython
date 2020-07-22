import webbrowser


condicion = False
buscadores = {
    'GOOGLE': {'general': "https://www.google.com/search?q=",
                'imagenes': "https://www.google.com/search?tbm=isch&q=",
                'videos': "https://www.google.com/search?tbm=vide&q=",
                'noticias': "https://www.google.com/search?tbm=nws&q=",
                'mapas': "https://www.google.com/maps?q="},
    'BING': {'general': "https://www.bing.com/search?q=",
              'imagenes': "https://www.bing.com/images/search?q=",
              'videos': "https://www.bing.com/videos/search?q=",
              'noticias': "https://www.bing.com/news/search?q="},
    'YAHOO': {'general': "https://espanol.search.yahoo.com/search?p=",
               'imagenes': "https://espanol.images.search.yahoo.com/search?p=",
               'video': "https://espanol.video.search.yahoo.com/search?p=",
               'noticias': "https://espanol.news.search.yahoo.com/search?p="},
    'DUCKDUCKGO': {'general': "https://duckduckgo.com/?q=",
                    'imagenes': "https://duckduckgo.com/?ia=images&q=",
                    'videos': "https://duckduckgo.com/?ia=videos&q=",
                    'noticias': "https://duckduckgo.com/?ia=news&q=",
                    'mapas': "https://duckduckgo.com/?iaxm=maps&q="},
    'BAIDU': {'general': "https://www.baidu.com/s?wd=",
              'imagenes': "http://image.baidu.com/search/index?tn=baiduimage&wd=",
                'videos': "https://www.baidu.com/sf/vsearch?pd=video&wd=",
                'noticias': "https://www.baidu.com/s?tn=news&wd=",
                'mapas': "map.baidu.com/search/asd/z?wd="}
}

while condicion == False:
    print("Por favor escriba el buscador a usar: \n Google \n Bing \n Yahoo \n DuckDuckDo \n Baidu")
    seleccion = input()
    seleccion = seleccion.upper()
    ##print(seleccion)
    for key in buscadores:
        ##print(str(key))
        if(seleccion == key):
            condicion = True
    if condicion == True:
        print("Buscador acpetado")
    if condicion == False:
        print("Opcion no valida, intente de nuevo")

print("Ingrese lo que desea buscar: ")
busqueda = input()
condicion = False

while condicion == False:
    print("Por favor escriba la opcion de busqueda: \n General \n Imagenes \n Videos \n Noticias \n Mapas")
    print("existe la posibilidad de que algun buscador no tenga alguna de las opciones ")
    opcion = input()
    opcion = opcion.lower()
    print(opcion)
    for key in buscadores[seleccion]:
        print(str(key))
        if (opcion == key):
            condicion = True
    if condicion == False:
        print("Opcion no valida, intente de nuevo")

print(buscadores[seleccion][opcion])
direccion = buscadores[seleccion][opcion] + busqueda
print(direccion)
webbrowser.open(direccion)
