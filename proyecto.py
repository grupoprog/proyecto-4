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
        dic = {}
        valores = linea.rstrip("\n").split(",")
        count = 0                  #contador para vincular cada dato a su respectivo identificador
        for atributo in identificadores:
            dic[atributo] = valores[count]
            count += 1
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