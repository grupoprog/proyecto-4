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

def fechaAtupla(fecha: str) -> tuple:
    '''
    str -> tuple[int,int,int,int]
    
    Dada una fecha como string, devuelve la misma fecha pasada a tupla.

    fechaAtupla("2025-10-02T06:00") == (2025,10,2,6)
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
    nombre_archivo: string

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
    donde la cantidad de veces que se encontro en la tabla es un int > 0 y la suma
    de los indices es un float >= 0.

    representamos los promedios de el valor a calcular de las ciudades (ciudades_promedios) como diccionarios de la forma
    {ciudad: promedio_indice}. donde promedio_indice es un float >= 0

    ciudades_filtradas -> ciudades_promedios

    Dado un diccionario con las ciudades filtradas, devuelve un diccionario con las ciudades y sus promedios de polvo/indice uv.
    '''
    for ciudad in ciudades_filtradas:
        cant_encuentros = ciudades_filtradas[ciudad][0]
        sum_ind = ciudades_filtradas[ciudad][1]

        ciudades_filtradas[ciudad] = sum_ind / cant_encuentros
    print("Promedios: " + str(ciudades_filtradas))
    return ciudades_filtradas

def ordenar_primeros_5(dic:dict[str:list]) -> dict[str:list]:
    """
    Funcion auxiliar para ordenar las primeros 5 ciudades de la funcion mayores_promedios
    Recibe un dic["ciudades":List[String], "promedios":List[Number]
    y produce el mismo tipo pero ordena simultaneamente ambas listas del diccionario
    """
    dic_aux={"ciudades":[dic["ciudades"][0]], "promedios":[dic["promedios"][0]]}
    dic["ciudades"].pop(0)
    dic["promedios"].pop(0) 
    for i in range(4):
        for j in range(len(dic_aux["ciudades"])):
            if dic["promedios"][i] > dic_aux["promedios"][j]:
                dic_aux["promedios"].insert(j,dic["promedios"][i])
                dic_aux["ciudades"].insert(j,dic["ciudades"][i])
                break
        if dic["ciudades"][i] not in dic_aux["ciudades"]:
            dic_aux["promedios"].append(dic["promedios"][i])
            dic_aux["ciudades"].append(dic["ciudades"][i])
    return dic_aux



def mayores_promedios(ciudades_promedios: dict[str:float]) -> dict[str:list]:
    '''
    Representamos los promedios de polvo de las ciudades (ciudades_promedios) como
    diccionarios de la forma {ciudad: promedio_polvo}. donde promedio_polvo es un float > 0
    Y los mayores promedios 

    Recibe los promedio de polvo y produce los 5 mayores promedios de polvo ordenados de mayor a menor con la
    lista de las ciudades tambien ordenada acorde a sus promedios
    '''
    nuevo_dic = {"ciudades":[], "promedios":[]}
    cuenta = 0
    flag_ordenado = False
    for ciudad in ciudades_promedios:
        flag = False
        cant_ciudades = len(nuevo_dic["ciudades"])

        if cuenta < 5 :
            nuevo_dic["ciudades"].append(ciudad)
            nuevo_dic["promedios"].append(ciudades_promedios[ciudad])
            cuenta += 1
            
        else:
            if not flag_ordenado: #en el primer else se deben ordenar los primeros 5
                nuevo_dic = ordenar_primeros_5(nuevo_dic)
                flag_ordenado=True
            count = 0
            for promedio in nuevo_dic["promedios"]:
                if ciudades_promedios[ciudad] > promedio and not flag:
                    nuevo_dic["promedios"] = nuevo_dic["promedios"][0:count] + [ciudades_promedios[ciudad]] + nuevo_dic["promedios"][count:4]
                    nuevo_dic["ciudades"] = nuevo_dic["ciudades"][0:count] + [ciudad] + nuevo_dic["ciudades"][count:4]
                    flag = True
                count += 1
    return nuevo_dic


def pregunta_1(tabla: list[dict], anio: int) -> dict[str: list]:
    '''
    representaremos los "mayores promedios" de las ciudades como
    dicccionarios de la forma {"ciudades": [nombres_ciudades], "Promedio": [promedios_polvo]}. 
    Donde las "nombres_ciudades" son strings y "promedios_polvo" son int. Ambas listas 
    son de 5 elementos

    tabla int -> mayores promedios
    
    Recibe una tabla y un año, y retorna un diccionario con las 5 ciudades con mayor promedio
    de indice de polvo.
    '''
    ciudades_filtradas = {}
    
    for fila in tabla:
        anio_fecha = fila["Timestamp"][0]
        ciudad = fila["City"]
        ind_polvo = fila["Dust_ug_m3"]

        if anio_fecha == anio:

            if ciudad in ciudades_filtradas:
                ciudades_filtradas[ciudad][0] += 1
                ciudades_filtradas[ciudad][1] += ind_polvo
            else:
                ciudades_filtradas[ciudad] = [1,ind_polvo]

    ciudades_promedios = mayores_promedios(promedio(ciudades_filtradas))
            
    return ciudades_promedios


def fecha_str(fecha: tuple) -> str:
    '''
    Dada una "fecha" de la tabla, devuelve el string con 
    el nombre del mes y año.
    '''
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    ind_mes = fecha[1] - 1
    mes_str = meses[ind_mes]
    año_str = str(fecha[0])

    return mes_str + " " + año_str

def elegir_color(prom_UV: float) -> str:
    '''
    Dado el "promedio de UV", devuelve el "color" como str en su
    forma Hexadesimal, según la siguiente forma:

    Verde: 0 <= prom_UV < 3
    Amarillo: 3 <= prom_UV < 6
    Naranja: 6 <= prom_UV < 8
    Rojo: 8 <= prom-UV < 11
    Violeta: 11 <= prom_UV
    '''
    color = ""
    if prom_UV < 3:
        color = "#0DFF00C8"
    elif prom_UV >= 3 and prom_UV < 6:
        color = "#FFFF00C8"
    elif prom_UV >= 6 and prom_UV < 8:
        color = "#FF9900C7"
    elif prom_UV >= 8 and prom_UV < 11:
        color = "#FF0000C7"
    else:
        color = "#C300FFC6"
    
    return color

def filtrar_ciudades(tabla: list[dict],anio: int,mes:int)-> dict[str: float]:
    '''dada una tabla, filtra ciudades segun el año y mes pasados y devuelve un diccionario de la forma:
    {ciudad:promedio_indice_uv}
    es decir cada ciudad queda asociada al promedio de indice uv durante el mes del año indicado
    '''
    ciudades_filtradas = {}
    
    for fila in tabla:
        anio_fecha = fila["Timestamp"][0]
        mes_fecha = fila["Timestamp"][1]
        ciudad = fila["City"]
        ind_uv = fila['UV_Index']

        if anio_fecha == anio and mes_fecha==mes:

            if ciudad in ciudades_filtradas:
                ciudades_filtradas[ciudad][0] += 1
                ciudades_filtradas[ciudad][1] += ind_uv
            else:
                ciudades_filtradas[ciudad] = [1,ind_uv]

    ciudades_promedios = (promedio(ciudades_filtradas))
            
    return ciudades_promedios

#def filtrar_ubicacionesXmes(tabla: list[dict]) -> dict[str: list[dict]]:
    '''
    Dada una "tabla", devuelve un diccionario de la forma {mes/año: ubicaciones} 
    donde la clave "mes/año" es un string con el nombre de mes y un año, y sus valores
    "ubicaciones" es una lista de diccionarios de la forma [{"latitude": float, "Longitude": float, "Color": str}].
    En donde, "Latitude" y "Longitude" son los valores correspondientes a los mismos de la tabla y el "Color" está 
    dado por el promedio de indices UV de cada ciudad en el "mes/año" correspondiente.
    '''

#    dic = {}
#    ubicacionesXmes = []
#    for fila in tabla:
#        fecha = fecha_str(fila["Timestamp"])
#        if fecha not in dic:
#            dic[fecha] = []
#        else:
#            dic[fecha].append()





def ejecutar_programa(tabla: list[dict]):
    '''
    Dada la tabla del dataset genera un link a la pagina web
    '''
    preg_1, preg_2 = st.tabs(["Pregunta 1", "Pregunta 2"], on_change = "rerun")

    if preg_1.open:
        st.title("¿Cuales fueron las 5 ciudades con mayor promedio de polvo en 2025?")
        st.table(pregunta_1(tabla, 2025))
    
    if preg_2.open:
        st.title("¿Cuál es el promedio de índice UV que tiene una ciudad en un mes X?")
        meses = ["Enero 2025", "Febrero 2025"]
        opcion = st.selectbox("Elija un mes", meses,)
        st.write("Mapa del promedio de UV en el mes de", opcion)
        # prueba del mapa:
        dic_prueba = {
            "Enero 2025": [{"Latitude": -34.6037, "Longitude": -58.3816, "Color":"#FFFF00C8"},
                           {"Latitude": 19.4326, "Longitude": -99.1332, "Color": "#0DFF00C8"}],
            "Febrero 2025": [{"Latitude": -34.6037, "Longitude": -58.3816, "Color":"#0DFF00C8"},
                             {"Latitude": 19.4326, "Longitude": -99.1332, "Color": "#FF0000C7"}]
        }
        st.map(dic_prueba[opcion], latitude = "Latitude", longitude = "Longitude", color = "Color", size = 40000)


def main():
    #python -m streamlit run proyecto.py para ejecutar la aplicación
    tabla = procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")
    ejecutar_programa(tabla)


if __name__ == "__main__":
    main()