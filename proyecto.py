import streamlit as st
'''
Representamos la tabla como una lista y cada fila de la tabla como {identificador: dato}
donde,
    identificador: (string) es el nombre de cada atributo de la tabla
    dato: (string) son los valores de las celdas de cada atributo correspondiente
'''

def procesar_archivo(nombre: str) -> list[dict]:
    '''
    archivo: string

    archivo -> tabla

    Recibe el nombre del archivo y produce una tabla con las entradas
    '''
    archivo = open(nombre)
    identificadores = archivo.readline().rstrip("\n").split(",")
    datos = []
    for linea in archivo:
        dic = {}
        valores = linea.rstrip("\n").split(",")
        count = 0
        for atributo in identificadores:
            dic[atributo] = valores[count]
            count += 1
        datos.append(dic)

    archivo.close()
    print(datos)

def main():
    procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")

if __name__ == "__main__":
    main()