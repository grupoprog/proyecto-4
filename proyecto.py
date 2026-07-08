# -------------------------------------------------------------------------------------------------------------------
# Trabajo Practico Grupal: Calidad del aire en distintas ciudades del mundo y niveles de polución.
# Catedra Programación II, 1C.
# Grupo 4
# Integrantes: Borraccini, Renzo.
#              Ruelli Cubertié, Jazmín.
#              Estibiarria, Tomás.
# Fecha: 18/6/2026
# -------------------------------------------------------------------------------------------------------------------
# Diseño de datos:

# Representamos una "tabla" (dataset) como una lista de diccionarios, donde cada
# diccionario es una "fila" de la tabla, siendo de la forma: [{atributo: valor}]

# En este caso, los "atributos" son los identificadores de cada columna, por lo que serán
# representados por Strings (ej: "Timestamp", "City", "European_AQI", etc.)

# los "valores" dependeran del atributo al que correspondan, siendo entonces:

# Fechas (Timestamp): Tuplas de la forma (Año,Mes,Dia,Hora), donde cada una 
# es un entero

# Ciudades (City): Strings

# Valores correspondientes a Latitude, Longitude, PM10_ug_m3, PM2_5_ug_m3, Carbon_Monoxide_ug_m3, 
# Nitrogen_Dioxide_ug_m3, Ozone_ug_m3, Dust_ug_m3, UV_Index: Float

# valores correspondientes a European_AQI, Hazardous_Event: Int 
# -------------------------------------------------------------------------------------------------------------------
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def fechaAtupla(fecha: str) -> tuple[int,int,int,int]:
    '''
    Dada una fecha como string, devuelve la misma fecha pasada a tupla.

    fechaAtupla("2025-10-02T06:00") == (2025,10,2,6)
    fechaAtupla("2025-09-30T23:00") == (2025,9,30,23)
    fechaAtupla("2026-02-08T01:00") == (2026,2,8,1)
    '''
    anio = int(fecha[0:4])
    mes = int(fecha[5:7])
    dia = int(fecha[8:10])
    hora = int(fecha[11:13]) 

    return (anio,mes,dia,hora)


def agregar_valor(fila: dict, atributo: str, valores: list[str], indice: int) -> dict:
    '''
    Dada una fila de la tabla (un diccionario), un atributo, una lista de valores y un índice, devuelve un diccionario.
    Si el atributo recibido es el tiempo, convierte el valor asociado en el diccionario (la string) a una tupla. 
    Si el atributo es la ciudad, el valor asociado en el diccionario queda como str.
    Si el atributo es European AQI o hazardous events, convierte el valor asociado en el diccionario (la string) a int.
    Si el atributo es otro, convierte el valor asociado en el diccionario (la string) a float.
    '''
    valor = valores[indice]

    if atributo == "Timestamp":
        fila[atributo] = fechaAtupla(valor)

    elif atributo == "City":
        fila[atributo] = valor

    elif atributo == "Hazardous_Event" or atributo == "European_AQI":
        fila[atributo] = int(valor)
    
    else: 
        fila[atributo] = float(valor)
    
    return fila


def crear_fila(atributos: list[str], valores: list[str]) -> dict:
    '''
    Dado una lista de atributos y una lista de valores, devuelve la 
    fila de la tabla.
    '''
    fila = {}
    i = 0
    for atributo in atributos:
        fila = agregar_valor(fila,atributo,valores,i)
        i += 1
    
    return fila


def procesar_archivo(nombre_archivo: str) -> list[dict]:
    '''
    archivo -> tabla

    Recibe el nombre del archivo y produce una tabla.
    '''
    archivo = open(nombre_archivo)
    atributos = archivo.readline().rstrip("\n").split(",")
    tabla = []
    for linea in archivo:          
        valores = linea.rstrip("\n").split(",")
        fila = crear_fila(atributos, valores)
        tabla.append(fila)

    archivo.close()
    return tabla


def promedio(ciudades_filtradas: dict[str:list]) -> dict[str:float]:
    '''
    Representamos a las "Ciudades filtradas" como diccionarios 
    de la forma {ciudad: [cantidad de veces encontrada, suma de indices de polvo/indice uv]}. 
    donde la cantidad de veces que se encontro en la tabla es un int > 0 y la suma de los indices es un float >= 0.

    representamos los promedios del valor a calcular de las ciudades (ciudades_promedios) como diccionarios de la forma
    {ciudad: promedio_indice}. donde promedio_indice es un float >= 0

    ciudades_filtradas -> ciudades_promedios

    Dado un diccionario con las ciudades filtradas, devuelve un diccionario con las ciudades y sus promedios de polvo/indice uv.

    promedio({'Paris': [10, 156.8], 'Tokyo':[4,16.4],'Beijing':[5,8.0], 'Seoul':[2,45.8] }) == 
    {'Paris': 15.680000000000001, 'Tokyo':4.1,'Beijing':1.6, 'Seoul':22.9 }
    promedio({'Buenos Aires': [1, 200.8], 'Mumbai':[7,234.8],'New York':[3,128.9], 'Seoul':[8,460.8] }) == 
    {'Buenos Aires': 200.8, 'Mumbai': 33.542857142857144, 'New York': 42.96666666666667, 'Seoul': 57.6}
    '''
    for ciudad in ciudades_filtradas:
        cant_encuentros = ciudades_filtradas[ciudad][0]
        sum_ind = ciudades_filtradas[ciudad][1]

        ciudades_filtradas[ciudad] = sum_ind / cant_encuentros
    
    return ciudades_filtradas

def ordenar_primeros_5(dic:dict[str:list],atributo:str) -> dict[str:list]:
    """
    Funcion auxiliar para ordenar las primeros 5 ciudades de la funcion mayores_promedios
    Recibe un dic["ciudades":List[String], "promedios":List[Number]
    y produce el mismo tipo pero ordena simultaneamente ambas listas del diccionario

    ordenar_primeros_5({'Ciudades': ['Tokyo', 'Beijing', 'Mumbai', 'Mexico City', 'Moscow'], 'promedios': [1.0, 14.0, 41.0, 1.0, 0.0]},
    "promedios") == {'Ciudades': [  'Mumbai','Beijing', 'Tokyo','Mexico City', 'Moscow'], 'promedios': [ 41.0, 14.0,1.0, 1.0, 0.0]}
    ordenar_primeros_5({'Ciudades': ['Tokyo', 'Beijing', 'Mumbai', 'Mexico City', 'Moscow'], 'promedios': [40.0, 22.0, 32.0, 99.0, 36.0]},
    "promedios") == {'Ciudades': [  'Mexico City','Tokyo', 'Moscow','Mumbai', 'Beijing'], 'promedios': [ 99.0, 40.0,36.0, 32.0, 22.0]}
    """
    dic_aux={"Ciudades":[dic["Ciudades"][0]], atributo:[dic[atributo][0]]} # pone los primeros elementos en el nuevo diccionario
    dic["Ciudades"].pop(0) # los saca del diccionario viejo
    dic[atributo].pop(0)
    insertado = False 
    for i in range(4): #por cada elemento del diccionario viejo
        for j in range(len(dic_aux["Ciudades"])): # los comparo uno a uno con los del diccionario nuevo
            if dic[atributo][i] > dic_aux[atributo][j] and not insertado: # si alguno es mayor y no fue insertado
                dic_aux[atributo].insert(j,dic[atributo][i]) #lo inserto en la posicion del indice determinado
                dic_aux["Ciudades"].insert(j,dic["Ciudades"][i])
                insertado = True
        insertado = False
        if dic["Ciudades"][i] not in dic_aux["Ciudades"]: # si no se inserto en el bucle anterior (ninguno es mayor), lo inserto al final
            dic_aux[atributo].append(dic[atributo][i])
            dic_aux["Ciudades"].append(dic["Ciudades"][i])
    return dic_aux


def mayores_valores(ciudades_valores: dict[str:float], atributo:str) -> dict[str:list]:
    '''
    Toma un diccionario de la forma {"ciudad":valor} donde el valor puede ser de distintas índoles
    tales como promedios, suma de eventos peligrosos, etc. Y toma un string representando el nombre de la columna de la tabla.
    Produce un diccionario de la forma {"ciudad":lista de ciudades, "atributo":lista de valores}
    en donde los indices de cada lista se corresponden y los cuales son los 5 mayores valores

    mayores_valores({'Paris':30.1,'Tokyo':10.4,'Seoul':5.20,'Beijing':4.3,'Mumbai':10.6,'Bangkok':8.0,'Moscow':0.0},"promedios") ==
     {'Ciudades':['Paris','Mumbai','Tokyo','Bangkok','Seoul'],'promedios':[30.1,10.6,10.4,8.0,5.20]}
    mayores_valores({'Paris':0.1,'Tokyo':0.4,'Seoul':5.20,'Beijing':6.3,'Mumbai':10.6,'Bangkok':8.0,'Moscow':0.0},"promedios") ==
     {'Ciudades':['Mumbai','Bangkok','Beijing','Seoul','Tokyo'],'promedios':[10.6,8.0,6.3,5.20,0.4]}
    '''
    nuevo_dic = {"Ciudades":[], atributo:[]}
    cuenta = 0
    flag_ordenado = False #bandera cuando los primeros 5 estan ordenados
    for ciudad in ciudades_valores: # se agregan los primeros 5 elementos del diccionario viejo al nuevo
        flag = False
        if cuenta < 5:
            nuevo_dic["Ciudades"].append(ciudad)
            nuevo_dic[atributo].append(ciudades_valores[ciudad])
            cuenta += 1

        else:
            if not flag_ordenado: #en el primer else se deben ordenar los primeros 5
                nuevo_dic = ordenar_primeros_5(nuevo_dic, atributo)
                flag_ordenado=True
            count = 0 
            for valor in nuevo_dic[atributo]: #por cada valor del diccionario viejo
                if ciudades_valores[ciudad] > valor and not flag:
                    nuevo_dic[atributo] = nuevo_dic[atributo][0:count] + [ciudades_valores[ciudad]] + nuevo_dic[atributo][count:4]
                    nuevo_dic["Ciudades"] = nuevo_dic["Ciudades"][0:count] + [ciudad] + nuevo_dic["Ciudades"][count:4]
                    flag = True
                count += 1
    return nuevo_dic


def contar_apariciones_y_sumar_elementos(fila: dict, atributo: str, dict_list: dict[list[int,float]], clave: str, condicion: bool) -> dict[list]:
    '''
    "dict_list" es un diccionario de listas donde el primer elemento es la cantidad de apariciones de un valor de una fila y el segundo
    es la suma de los elementos encontrados de la fila.

    Dada una tabla, un atributo de la misma, un diccionario de listas, una clave y una condición, en base a la condición, si esta es verdadera,
    modifica al diccionario de listas dado, si no, devuelve al mismo sin ningún cambio.
    La modificación del diccionario va a ser, la inclusión de la clave dada con la lista, formada por el incio de conteo de apariciones del elemento de 
    la fila (en este caso el número 1) y el mismo elemento. Si en cambio, está clave está en el diccionario, se suma 1 al contador de apariciones
    y se suma el elemento encontrado a la suma de los elementos.

    contar_apariciones_y_sumar_elementos(
                                        {'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 
                                        'PM2_5_ug_m3': 36.9, 'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 
                                        'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1},
                                        "Dust_ug_m3",
                                        {},
                                        "Delhi",
                                        True
                                        ) = {"Delhi": [1,176.0]}
    contar_apariciones_y_sumar_elementos(
                                        {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 
                                        'PM2_5_ug_m3': 154.6, 'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 
                                        'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1},
                                        "Dust_ug_m3",
                                        {"Delhi": [1,176.0]},
                                        "Beijing",
                                        True 
                                        ) = {"Delhi": [1,176.0], "Beijing": [1, 14.0]}
    contar_apariciones_y_sumar_elementos(
                                        {'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 
                                        'PM2_5_ug_m3': 36.9, 'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 
                                        'Dust_ug_m3': 134.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1},
                                        "Dust_ug_m3",
                                        {"Delhi": [1,176.0], "Beijing": [1, 14.0]},
                                        "Delhi",
                                        True
                                        ) = {"Delhi": [2,310.0], "Beijing": [1, 14.0]}
    '''
    atributo_individual = fila[atributo]
    if condicion:
        if clave in dict_list:
            dict_list[clave][0] += 1
            dict_list[clave][1] += atributo_individual
        else:
            dict_list[clave] = [1, atributo_individual]
    
    return dict_list


def filtrar_por_anio_y_suma(tabla: list[dict],anio:int,atributo:str)->dict[str:list[int,float]]:
    """
    Recibe una tabla, un año y un atributo y produce un diccionario de la forma {ciudad:[numero_de_entradas,suma_de_valores]}
    la misma es la que se usa para luego aplicar la funcion promedio
    """
    ciudades_filtradas = {}
    for fila in tabla:
        anio_fecha = fila["Timestamp"][0]
        ciudad = fila["City"]
        condicion = anio_fecha == anio

        ciudades_filtradas = contar_apariciones_y_sumar_elementos(fila, atributo, ciudades_filtradas, ciudad, condicion)
        
    return ciudades_filtradas


def pregunta_1(tabla: list[dict], anio: int) -> dict[str: list]:
    '''
    representaremos los "mayores promedios" de las ciudades como dicccionarios de la forma 
    {"ciudades": [nombres_ciudades], "Promedio": [promedios_polvo]}. 
    Donde las "nombres_ciudades" son strings y "promedios_polvo" son int. Ambas listas son de 5 elementos

    tabla int -> mayores promedios
    
    Recibe una tabla y un año, y retorna un diccionario con las 5 ciudades con mayor promedio de indice de polvo.
    '''
    ciudades_promedios = mayores_valores(promedio(filtrar_por_anio_y_suma(tabla,anio,"Dust_ug_m3")), "Promedios")
            
    return ciudades_promedios


def fecha_str(fecha: tuple) -> str:
    '''
    Fecha(tupla) -> Fecha("Mes año")

    Dada una "fecha" de la tabla, devuelve el string con 
    el nombre del mes y año.

    fecha_str((2025, 1, 10, 9)) == "Enero 2025"
    fecha_str((2025, 8, 2, 15)) == "Agosto 2025"
    fecha_str((2026, 5, 27, 18)) == "Mayo 2026"
    '''
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    ind_mes = fecha[1] - 1
    mes_str = meses[ind_mes]
    anio_str = str(fecha[0])

    return mes_str + " " + anio_str


def elegir_color(prom_UV: float) -> str:
    '''
    prom_UV -> Color

    Dado el "promedio de UV", devuelve el "color" como str en su forma Hexadesimal, según la siguiente forma:

    Verde: 0 <= prom_UV < 1
    Amarillo: 1 <= prom_UV < 2
    Naranja: 2 <= prom_UV < 3
    Rojo: 3 <= prom-UV < 4
    Violeta: 4 <= prom_UV

    (La escala de los colores no es la que se suele usar en general, se modificó para que sea más visual el cambio de colores).

    elegir_color(15.0) == "#C300FFC6"
    elegir_color(1.65) == "#FFFF00C8"
    elegir_color(0.0) == "#0DFF00C8"
    '''
    color = ""
    if prom_UV < 1:
        color = "#0DFF00C8"
    elif prom_UV >= 1 and prom_UV < 2:
        color = "#FFFF00C8"
    elif prom_UV >= 2 and prom_UV < 3:
        color = "#FF9900C7"
    elif prom_UV >= 3 and prom_UV < 4:
        color = "#FF0000C7"
    else:
        color = "#C300FFC6"
    
    return color


def filtrar_ciudades(tabla: list[dict], fecha: str)-> dict[str: tuple]:
    '''
    dada una tabla y una fecha dada como string de la forma "mes año", filtra ciudades segun el año y mes pasados 
    y devuelve un diccionario de la forma: {ciudad:(latitud,longitud,promedio_indice_uv)}.
    Es decir cada ciudad queda asociada a sus coordenadas y al promedio de indice uv durante el mes del año indicado
    '''
    ciudades_filtradas = {}
    ubicaciones = {}
    
    for fila in tabla:
        fecha_fila = fecha_str(fila["Timestamp"])
        ciudad = fila["City"]
        condicion = fecha == fecha_fila

        ciudades_filtradas = contar_apariciones_y_sumar_elementos(fila, 'UV_Index', ciudades_filtradas, ciudad, condicion)
        
        latitud = fila["Latitude"]
        longitud = fila["Longitude"]
        
        if ciudad not in ubicaciones:
            ubicaciones[ciudad] = (latitud,longitud)

    ciudades_promedios = promedio(ciudades_filtradas)

    promedios_ubicaciones = {}

    for ciudad in ciudades_promedios:
        latitud = ubicaciones[ciudad][0]
        longitud = ubicaciones[ciudad][1]
        promed = ciudades_promedios[ciudad]
        promedios_ubicaciones[ciudad] = (latitud, longitud, promed)
            
    return promedios_ubicaciones


def filtrar_ubicacionesXmes(tabla: list[dict], fecha: str) -> list[dict]:
    '''
    Dada una "tabla" y una fecha en la forma "mes año", devuelve ubicaciones,
    una lista de diccionarios de la forma [{"Latitude": float, "Longitude": float, "Color": str}].
    En donde, "Latitude" y "Longitude" son los valores correspondientes a los mismos de la tabla y el "Color" está 
    dado por el promedio de indices UV de cada ciudad en el mes y año correspondiente.
    '''
    ciudades_promedios = filtrar_ciudades(tabla, fecha)
    
    lista = []
    for ciudad in ciudades_promedios:
        latitud = ciudades_promedios[ciudad][0]
        longitud = ciudades_promedios[ciudad][1]
        promedio = ciudades_promedios[ciudad][2]

        lista.append({"Latitude": latitud, "Longitude": longitud, "Color": elegir_color(promedio)})
    
    return lista


def ciudad_america(ciudad:str)->bool:
    '''dada una ciudad devuelve True si es de America

    ciudad_america('Mexico City') == True
    ciudad_america('Tokyo') == False'''
    lista_ciudades_america=['New York','Chicago','Los Angeles','Mexico City','Bogota','Lima','Sao Paulo','Buenos Aires']
    return ciudad in lista_ciudades_america


def filtrar_ciudades_america(tabla:list[dict])->list[dict]:
    '''dada una tabla devuelve una version reducida que incluye los datos unicamente de las ciudades de América'''
    nueva=[]
    for fila in tabla:
        if ciudad_america(fila['City']):
            nueva.append(fila)
    return nueva

def pregunta_3(tabla: list[dict], anio: int) -> dict[str: list]:
    '''
    representaremos los "mayores promedios" de las ciudades como
    dicccionarios de la forma {"ciudades": [nombres_ciudades], "Promedio": [promedios_pm25]}. 
    Donde las "nombres_ciudades" son strings y "promedios_pm25" son float. Ambas listas 
    son de 5 elementos

    tabla int -> mayores promedios
    
    Recibe una tabla y un año, y retorna un diccionario con las 5 ciudades de america on mayor promedio de PM 2.5.
    '''
    tabla_america = filtrar_ciudades_america(tabla)
    ciudades_promedios = mayores_valores(promedio(filtrar_por_anio_y_suma(tabla_america,anio,"PM2_5_ug_m3")),"Promedios")
            
    return ciudades_promedios


def ejecutar_pregunta3(tabla: list[dict]):
    '''
    Produce los componentes de la pregunta 3 en la pagina
    '''
    st.title("¿Cuáles son las 5 ciudades de América con mayor cantidad de PM2.5 en 2025?")

    dic= pregunta_3(tabla,2025)
    x=dic["Ciudades"]
    y=dic["Promedios"]
    bar_colors = ['#FF3434', '#FF8059', '#FF9756','#F5AD6A','#FFEB7C']

    fig, ax = plt.subplots()
    ax.bar(x, y, color=bar_colors)

    ax.set_title("5 ciudades de América con mayor promedio de PM2.5 en 2025")
    ax.set_xlabel("Ciudades")
    ax.set_ylabel("Promedios")

    st.pyplot(fig)


def ejecutar_pregunta1(tabla: list[dict]):
    '''
    Produce los componentes de la pregunta 1 en la pagina
    '''

    st.title("¿Cuales fueron las 5 ciudades con mayor promedio de polvo en 2025?")
    st.table(pregunta_1(tabla, 2025))


def colores_ind_uv(list_colores: list, etiquetas: list, ncols: int = 5):
    '''
    Realiza una descripcion de los significados de cada color de los indices UV
    '''
    cell_width = 180
    cell_height = 22
    swatch_width = 30
    margin = 5

    n = len(etiquetas)
    nrows = pat.math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 80

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(etiquetas):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            pat.Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=list_colores[i], edgecolor='0.7')
        )

    return fig


def ejecutar_pregunta2(tabla: list[dict]):
    '''
    Permite la entrada de la fecha y produce los componentes de la pregunta 2 en la pagina
    '''
    st.title("¿Cuál es el promedio de índice UV que tiene una ciudad en un mes X?")

    meses = ["Mayo 2025", "Junio 2025", "Julio 2025","Agosto 2025", "Septiembre 2025", "Octubre 2025", 
             "Noviembre 2025", "Diciembre 2025", "Enero 2026","Febrero 2026", "Marzo 2026",
             "Abril 2026", "Mayo 2026"]
    
    opcion = st.selectbox("Elija un mes:", meses)
    st.write("Mapa del promedio de UV en el mes de", opcion)

    colores = ["#0DFF00C8","#FFFF00C8","#FF9900C7","#FF0000C7","#C300FFC6"]
    etiquetas = ["Bajo", "Moderado", "Alto", "Muy alto", "Extremo"]

    fig = colores_ind_uv(colores, etiquetas)

    st.pyplot(fig)
        
    ubicaciones_promedios = filtrar_ubicacionesXmes(tabla, opcion)
        
    st.map(ubicaciones_promedios, latitude = "Latitude", longitude = "Longitude", color = "Color", size = 40000)

def lat_long_validas(lat_sup:int,lat_inf:int,long_inf:int,long_sup:int, lat_ingresada:int, long_ingresada:int)-> bool:
    '''verifica si las coordenadas geogeraficas ingresadas por el usuario son correctas
    
    lat_long_validas(100,0,0,100,-5,500) == False
    lat_long_validas(100,0,0,100,50,20) == True'''
    return ((lat_inf < lat_ingresada) and (lat_sup > lat_ingresada) and (long_inf < long_ingresada) and (long_sup > long_ingresada))

def filtrar_por_ubicacion(tabla,lat_sup:int,lat_inf:int,long_inf:int,long_sup:int)-> dict[str:int]:
    '''
    Recibe una tabla y la filtra según latitud inferior y superior, y longitud inferior y superior.
    Produce un un diccionario de la forma {ciudad : cantidad de eventos catastroficos}
    '''
    tabla_filtrada={}
    for entrada in tabla:
        if lat_long_validas(lat_sup,lat_inf,long_inf,long_sup, entrada["Latitude"], entrada["Longitude"]):
            if entrada["City"] in tabla_filtrada:
                tabla_filtrada[entrada["City"]]+=entrada["Hazardous_Event"]
            else:
                tabla_filtrada[entrada["City"]] = entrada["Hazardous_Event"]
    return tabla_filtrada


def coordenadas_validas(lat_sup:float,lat_inf:float,long_sup:float,long_inf:float)->bool:
    '''
    Interpretamos las coordenadas de latitud (entre -90 y 90) o longitud(entre -180 y 180) como floats.
    Recibe coordenadas que representa la latitud superior, inferior, la longitud superior e inferior. 
    Produce un booleano en funcion si la longitud inferior es menor a la latitud superior y de igual manera con las longitudes.

    coordenadas_validas(12.2,7,-55,13) == False
    coordenadas_validas(55,-1.3,125,120) == True
    coordenadas_validas(0,0,0,0) == False
    '''
    return lat_inf<lat_sup and long_inf<long_sup

def confirmar_datos(tabla,lat_sup:float,lat_inf:float,long_inf:float,long_sup:float):
    '''
    Esta función toma los valores de entrada del usuario de la pregunta 4, verifica que sean válidos y produce la tabla de valores,
    lista para ser renderizada en la página.
    '''
    if coordenadas_validas(lat_sup,lat_inf,long_sup,long_inf):
        st.table(mayores_valores(filtrar_por_ubicacion(tabla,lat_sup,lat_inf,long_inf,long_sup),"Eventos Peligrosos"))
    else:
        st.write("Valores inválidos.")
        


def ejecutar_pregunta4(tabla):
    """
    Funcion encargada de el ingreso de datos del usuario y la renderización de los componentes de la pregunta 4.
    """
    st.title("¿Qué 5 ciudades entre las latitudes X y longitudes X tuvieron mayor cantidad de días con eventos peligrosos en 2025?")
    st.write("Ingrese valores entre -90 y 90 para la latitud y entre -180 y 180 para la longitud. De manera que la latitud inferior\
     sea menor a la latitud superior y la longitud inferior sea menor a la longitud superior.")
    latitud_inferior = st.slider("Latitud Inferior", -90, 90)
    latitud_superior = st.slider("Latitud Superior", -90, 90)
    longitud_inferior = st.slider("Longitud Inferior", -180, 180)
    longitud_superior = st.slider("Longitud Superior", -180, 180)

    if st.button("Buscar"):
        resultado = confirmar_datos(
            tabla,
            latitud_superior,
            latitud_inferior,
            longitud_inferior,
            longitud_superior
        )
        st.write(resultado)
        

def listar_por_atributo(tabla: list[dict], atributo: str) -> list:
    '''
    tabla atributo -> lista

    Dada una "tabla" y un "atributo", devuelve una lista de los elementos que corresponde a ese atributo
    sin repetir elementos.
    '''
    lista = []

    for fila in tabla:
        valor = fila[atributo]
        if valor not in lista:
            lista.append(valor)
    
    return lista


def filtrar_promedio_ciudades_por_fecha(tabla: list[dict], atributo: str, fecha: str) -> dict[str: float]:
    '''
    tabla atributo fecha("mes año") -> {ciudad: promedio}

    Dada una tabla, un atributo y una fecha de la forma "mes año", devuelve un diccionario
    cuyas claves son los nombres de las ciudades y sus valores son el promedio
    correspondiente al atributo de la ciudad en la fecha dada.
    '''
    ciudades_filtradas = {}
    for fila in tabla:
        fecha_fila = fecha_str(fila["Timestamp"])
        componente = fila[atributo]
        ciudad = fila["City"]

        if fecha == fecha_fila:
            if ciudad in ciudades_filtradas:
                ciudades_filtradas[ciudad][0] += 1
                ciudades_filtradas[ciudad][1] += componente
            else:
                ciudades_filtradas[ciudad] = [1,componente]
    
    promedio_ciudades = promedio(ciudades_filtradas)

    return promedio_ciudades

def aux(dic_ciudad_prom: dict, componente:str,dic: dict)-> dict[str:list[float]]:
    '''toma un diccionario de la forma {'ciudad':promedio de atributo dado} y componente
    y para cada ciudad en el diccionario recibido como argumento, va agregando un elemento a la lista (el promedio del componente dado)
    por ejemplo, al filtrar el promedio de "PM10_ug_m3" en  "Diciembre 2025" de una tabla dada, tenemos que 
    dic_ciudad_prom={"Delhi": 129.5, "Beijing": 164.4}
    aux({"Delhi": 129.5, "Beijing": 164.4},"PM10_ug_m3")=={"Delhi":[129.5], "Beijing":[164.4]} '''
    for ciudad in dic_ciudad_prom:
        promedio = dic_ciudad_prom[ciudad]

        if ciudad in dic:
            dic[ciudad].append(promedio)
        else:
            dic[ciudad] = [promedio]

    return dic

def promedios_componentes_de_ciudades(tabla: list[dict], fecha: str) -> dict[str:list[float]]:
    '''
    tabla fecha -> {ciudad: [promedios]}

    Dada una tabla y una fecha de la forma "mes año", devuelve un diccionario cuyas claves son
    los nombres de las ciudades y sus valores son listas (ordenadas) de los promedios de
    las componentes del aire correspondientes a la misma en la fecha dada.
    '''
    dic = {}
    
    componentes = ["PM10_ug_m3", "PM2_5_ug_m3", "Carbon_Monoxide_ug_m3", "Nitrogen_Dioxide_ug_m3","Ozone_ug_m3", "Dust_ug_m3"]
    
    for componente in componentes:
        promedios_componente = filtrar_promedio_ciudades_por_fecha(tabla,componente,fecha)
        dic=aux(promedios_componente,componente,dic)
        
    return dic


def ejecutar_pregunta5(tabla: list[dict]):
    '''
    Permite la entrada del mes y ciudad deseada y produce la ejecución pregunta 5
    '''
    st.title("¿Cuáles son las componentes del aire en X ciudad en un mes Y?")

    meses = ["Mayo 2025", "Junio 2025", "Julio 2025","Agosto 2025", "Septiembre 2025", "Octubre 2025", 
             "Noviembre 2025", "Diciembre 2025", "Enero 2026","Febrero 2026", "Marzo 2026",
             "Abril 2026", "Mayo 2026"]

    opcion_1 = st.selectbox("Elija un mes:", meses)

    ciudades = listar_por_atributo(tabla, "City")

    opcion_2 = st.selectbox("Elija una ciudad:", ciudades)
    st.write("Componentes del aire de ", opcion_2, " en el mes de ", opcion_1)

    fig, ax = plt.subplots(figsize = (6,3))

    promedios = promedios_componentes_de_ciudades(tabla,opcion_1)[opcion_2]

    componentes = ["PM10_ug_m3", "PM2_5_ug_m3", "Carbon_Monoxide_ug_m3", "Nitrogen_Dioxide_ug_m3",
                   "Ozone_ug_m3", "Dust_ug_m3"]

    ax.pie(promedios, autopct = "%1.1f%%\n", pctdistance = 1.17, textprops = dict(size = 5))

    ax.legend(componentes, title = "Componentes",
              loc = "center left", bbox_to_anchor=(1, 0, 0.5, 1))

    st.pyplot(fig)


def promedios_monoxido_por_mes(ciudad:str,tabla:list[dict])->list[float]:
    """
    Recibe una ciudad y una tabla y produce una lista de la forma [prom 01/25,prom 02/25, ... ,prom 05/26]}
    es decir para una ciudad dada, calcula el promedio de monoxido de carbono para cada mes (entre Mayo 2025-Mayo 2026)
    y lo va agregando a una lista de forma ordenada
    """
    meses = ["Mayo 2025", "Junio 2025", "Julio 2025","Agosto 2025", "Septiembre 2025", "Octubre 2025", "Noviembre 2025", "Diciembre 2025", 
    "Enero 2026","Febrero 2026", "Marzo 2026", "Abril 2026", "Mayo 2026"]
    l=[]
    for mes in meses:
        dic=promedios_componentes_de_ciudades(tabla,mes)
        prom_monoxido_por_mes=dic[ciudad][2]
        #al aplicar promedios_componentes_de_ciudades, esta devuelve un diccionario donde cada ciudad queda asociada a una lista de
        #promedios de cada uno de los indices y el monoxido de carbono esta en la posicion 2
        #{'ciudad':["PM10_ug_m3", "PM2_5_ug_m3", "Carbon_Monoxide_ug_m3", "Nitrogen_Dioxide_ug_m3","Ozone_ug_m3", "Dust_ug_m3"]}
        l.append(prom_monoxido_por_mes)
    return l

def pregunta_6(tabla: list[dict])->dict[str:list[float]]:
    """
    Recibe una tabla y un atributo y produce un diccionario de la forma {ciudad:[prom 01/25,prom 02/25, ... ,prom 05/26]}
    es decir cada ciudad queda asociada a una lista donde cada elemento de esta sera el promedio de monoxido de carbono correspondiente a cada mes
    """
    ciudades = listar_por_atributo(tabla, "City")
    nuevo_dic={}
    for ciudad in ciudades:
        nuevo_dic[ciudad]=promedios_monoxido_por_mes(ciudad,tabla)
    return nuevo_dic

def ejecutar_pregunta6(tabla: list[dict]):
    '''Produce los componentes de la pregunta 6 en la pagina'''
    st.title("¿Cuál es el promedio de monóxido de carbono en X ciudad a lo largo de los meses?")

    ciudades = listar_por_atributo(tabla, "City")
    meses = ["5\n25", "6\n25", "7\n25","8\n25", "9\n25", "10\n25", "11\n25", "12\n25", "1\n26","2\n26", "3\n26", "4\n26", "5\n26"]

    ciudad_elegida = st.selectbox("Elija una ciudad:", ciudades)

    dic=pregunta_6(tabla)
    x=meses
    y=dic[ciudad_elegida]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='meses', ylabel='promedio de monoxido de carbono', title='Evolución del promedio de monóxido de carbono durante Mayo 2025-Mayo 2026')
    ax.grid()

    st.pyplot(fig)


def ejecutar_programa(tabla: list[dict]):
    '''
    Dada la tabla del dataset genera un link a la pagina web
    '''
    preg_1, preg_2, preg_3, preg_4, preg_5, preg_6= st.tabs(["Pregunta 1", "Pregunta 2", "Pregunta 3", "Pregunta 4", "Pregunta 5", "Pregunta 6"], on_change = "rerun")
    
    if preg_1.open:
        ejecutar_pregunta1(tabla)
    if preg_2.open:
        ejecutar_pregunta2(tabla)
    if preg_3.open:
        ejecutar_pregunta3(tabla)
    if preg_4.open:
        ejecutar_pregunta4(tabla)
    if preg_5.open:
        ejecutar_pregunta5(tabla)
    if preg_6.open:
        ejecutar_pregunta6(tabla)

def main():
    #python -m streamlit run proyecto.py para ejecutar la aplicación
    tabla = procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")
    ejecutar_programa(tabla)


if __name__ == "__main__":
    main()