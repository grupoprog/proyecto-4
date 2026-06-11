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
    
    Dada una fecha como string, devuelve la misma fecha 
    pasada a tupla.

    fechaAtupla("2025-10-02 6:00")
    '''
    anio = int(fecha[0:4])
    mes = int(fecha[5:7])
    dia = int(fecha[8:10])
    hora = int(fecha[11:13]) 

    return (anio,mes,dia,hora)


def agregar_valor(linea: dict, atributo: str, valores: list[str], indice: int) -> dict:
    '''Dada una fila de la tabla (un diccionario), un atributo, una lista de valores y un índice, devuelve un diccionario.
    Si el atributo recibido es el tiempo, convierte el valor asociado en el diccionario (la string) a una tupla. 
    Si el atributo es latitud, longitud, PM 10, PM 2.5, dióxido de nitrógeno o índice UV, convierte el valor asociado en el diccionario (la string) a float. 
    Si el atributo es monóxido de carbono, ozono, polvo, European AQI o hazardous events, convierte el valor asociado en el diccionario (la string) a int.
'''
    valor = valores[indice]

    if atributo == "Timestamp":
        linea[atributo] = fechaAtupla(valor)

    elif atributo == "City":
        linea[atributo] = valor

    elif atributo == "Hazardous_Event" or atributo == "European_AQI":
        linea[atributo] = int(valor)
    
    else: 
        linea[atributo] = float(valor)
    
    return linea


def crear_linea(identificadores: list[str], valores: list[str]) -> dict:
    '''
    Dado una lista de atributos y una lista de valores, devuelve una 
    linea de la tabla cuyos valores están en 
    '''
    linea = {}
    i = 0
    for atributo in identificadores:
        linea = agregar_valor(linea,atributo,valores,i)
        i += 1
    
    return linea


def procesar_archivo(nombre: str) -> list[dict]:
    '''
    archivo: string

    archivo -> tabla

    Recibe el nombre del archivo y produce una tabla con las entradas.
    '''
    archivo = open(nombre)
    identificadores = archivo.readline().rstrip("\n").split(",")     # obtengo los identificadores
    datos = []
    for linea in archivo:          
        valores = linea.rstrip("\n").split(",")
        linea = crear_linea(identificadores, valores)
        datos.append(linea)

    archivo.close()
    return datos

def promedio(dic):
    for e in dic:
        dic[e]=dic[e][1]/dic[e][0]
    return dic
def mayores_promedios(dic):
    nuevo_dic={"ciudades":[],
                "promedios":[]}
    for e in dic:
        flag = False
        if len(nuevo_dic["ciudades"]) < 5:
            nuevo_dic["ciudades"].append(e)
            nuevo_dic["promedios"].append(dic[e])
            print(nuevo_dic["promedios"])
        else:
            for el in nuevo_dic["promedios"]:
                count = 0
                if dic[e] > el and not flag:
                    nuevo_dic["promedios"]=nuevo_dic["promedios"][0:count]+ [dic[e]] + nuevo_dic["promedios"][count:4]
                    nuevo_dic["ciudades"]=nuevo_dic["ciudades"][0:count]+ [e] + nuevo_dic["ciudades"][count:4]
                    flag = True
                count += 1
    return nuevo_dic

def filtrar_por_año(tabla: list[dict],año: int) -> list[dict]:
    """
    tabla entero -> tabla
    
    Recibe una tabla y un año, y produce una tabla con todas las entradas coincidentes a ese año
    """
    lista_nueva = {}
    
    for e in tabla:
        if  e["Timestamp"][:4] == año:
            if e["City"] in lista_nueva:
                lista_nueva[e["City"]][0] += 1
                lista_nueva[e["City"]][1] += float(e["Dust_ug_m3"])
            else:
                lista_nueva[e["City"]]=[1,float(e["Dust_ug_m3"])]

            #lista_nueva.append(e)
    return mayores_promedios(promedio(lista_nueva))

def pregunta_1():

    st.title("")
def main():
    #python -m streamlit run proyecto.py para ejecutar la aplicación
    #tabla = procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")
    tabla = procesar_archivo("tabla_para_tests.csv")
    print(filtrar_por_año(tabla, "2025"))
    # ejemplo para tabla:
    #ejemplo = [{"Nombre": "Pedrito", "Edad":14, "Le gusta jugar?":"si"},
    #{"Nombre": "Ramon", "Edad":66, "Le gusta jugar?":"no"},
   # {"Nombre": "Oscar", "Edad":56, "Le gusta jugar?":"no"}]
    #con la siguiente funcion ya se ve una tabla en la pagina
    #st.table(ejemplo)


if __name__ == "__main__":
    main()