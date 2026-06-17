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
    de la forma {ciudad: [cantidad de veces encontrada, suma de indices de polvo]}. 
    donde la cantidad de veces que se encontro en la tabla es un int > 0 y la suma
    de los indices de polvo es un float >= 0.

    representamos los promedios de polvo de las ciudades (ciudades_promedios) como diccionarios de la forma
    {ciudad: promedio_polvo}. donde promedio_polvo es un float >= 0

    ciudades_filtradas -> ciudades_promedios

    Dado un diccionario con las ciudades filtradas, devuelve un diccionario
    con las ciudades y sus promedios de polvo.
    '''
    for ciudad in ciudades_filtradas:
        cant_encuentros = ciudades_filtradas[ciudad][0]
        sum_ind_polvo = ciudades_filtradas[ciudad][1]

        ciudades_filtradas[ciudad] = sum_ind_polvo / cant_encuentros

    return ciudades_filtradas


def mayores_promedios(ciudades_promedios: dict[str:float]) -> dict[str:list]:
    '''
    Representamos los promedios de polvo de las ciudades (ciudades_promedios) como
    diccionarios de la forma {ciudad: promedio_polvo}. donde promedio_polvo es un float > 0
    Y los mayores promedios 

    Recibe los promedio de polvo y produce los 5 mayores promedios de polvo ordenados de mayor a menor
    '''
    nuevo_dic = {"ciudades":[], "promedios":[]}
    
    for ciudad in ciudades_promedios:
        flag = False
        cant_ciudades = len(nuevo_dic["ciudades"])

        if cant_ciudades < 5:
            nuevo_dic["ciudades"].append(ciudad)
            nuevo_dic["promedios"].append(ciudades_promedios[ciudad])
            
        else:
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

    ciudades_promedios = promedio(ciudades_filtradas)
            
    return mayores_promedios(ciudades_promedios)


def ejecutar_programa(tabla: list[dict]):
    '''
    Dada la tabla del dataset genera un link a la pagina web
    '''
    acceder_pregunta_1 = False
    acceder_pregunta_2 = False

    with st.sidebar:
        if st.button("¿Cuales fueron las 5 ciudades con mayor promedio de polvo en 2025?", type = "tertiary"):
            acceder_pregunta_1 = True
        if st.button("Hola"):
            acceder_pregunta_2 = True

    if acceder_pregunta_1:
        st.title("¿Cuales fueron las 5 ciudades con mayor promedio de polvo en 2025?")
        st.table(pregunta_1(tabla, 2025))
    
    if acceder_pregunta_2:
        st.write("Hola!")


def main():
    #python -m streamlit run proyecto.py para ejecutar la aplicación
    tabla = procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")
    #tabla = procesar_archivo("tabla_para_tests.csv")
    #print(pregunta_1(tabla, 2025))
    #ejemplo para tabla:
    #ejemplo = [{"Nombre": "Pedrito", "Edad":14, "Le gusta jugar?":"si"},
    #{"Nombre": "Ramon", "Edad":66, "Le gusta jugar?":"no"},
    #{"Nombre": "Oscar", "Edad":56, "Le gusta jugar?":"no"}]
    #con la siguiente funcion ya se ve una tabla en la pagina
    #st.table(ejemplo)
    ejecutar_programa(tabla)


if __name__ == "__main__":
    main()