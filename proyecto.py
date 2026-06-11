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

# Valores correspondientes a Latitude, Longitude, PM10_ug_m3, PM2_5_ug_m3, Nitrogen_Dioxide_ug_m3, UV_Index: Float

# valores correspondientes a Carbon_Monoxide_ug_m3, Ozone_ug_m3, Dust_ug_m3, European_AQI, Hazardous_Event: Int 
# -------------------------------------------------------------------------------------------------------------------
import streamlit as st

def fechaAtupla(fecha):
    '''str -> tuple[int,int,int,int] 

    dada una fecha en forma de string, devuelve una tupla de la forma (Año,Mes,Dia,Hora)
    
    ejemplos:
    fechaAtupla("2025-10-02T06:00")==(2025,10,2,6)
    fechaAtupla("2026-02-15T13:00")==(2026,2,15,13)
    fechaAtupla("2025-09-30T23:00")==(2025,9,30,23)
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

    elif atributo == "Latitude" or atributo == "Longitude" or atributo == "PM10_ug_m3" or atributo == "PM2_5_ug_m3" or 
         atributo == "Nitrogen_Dioxide_ug_m3" or atributo == "UV_Index":
        linea[atributo] = float(valor)

    elif atributo == "Carbon_Monoxide_ug_m3" or atributo == "Ozone_ug_m3" or atributo == "Dust_ug_m3" or atributo == "European_AQI" or 
         atributo == "Hazardous_Event" or atributo == "UV_Index":
         linea[atributo] = int(valor)
    
    else: 
        linea[atributo] = valor
    
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
        crear_linea(identificador, valores)
        datos.append(dic)

    archivo.close()
    return datos


def filtrar_por_año(tabla: list[dict],año: int) -> list[dict]:
    """
    tabla entero -> tabla
    
    Recibe una tabla y un año, y produce una tabla con todas las entradas coincidentes a ese año
    """
    lista_nueva = []
    for e in tabla:
        if  e["Timestamp"][:4] == año:
            lista_nueva.append(e)
    return lista_nueva


def main():
    #python -m streamlit run app.py para ejecutar la aplicación
    #tabla = procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")
    tabla = procesar_archivo("tabla_para_tests.csv")
    print(filtrar_por_año(tabla, "2025"))
    # ejemplo para tabla:
    #ejemplo = [{"Nombre": "Pedrito", "Edad":14, "Le gusta jugar?":"si"},
    #{"Nombre": "Ramon", "Edad":66, "Le gusta jugar?":"no"},
    #{"Nombre": "Oscar", "Edad":56, "Le gusta jugar?":"no"}]
    #con la siguiente funcion ya se ve una tabla en la pagina
    #st.table(ejemplo)


if __name__ == "__main__":
    main()