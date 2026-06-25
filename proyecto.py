# -------------------------------------------------------------------------------------------------------------------
# Trabajo Practico Grupal: Calidad del aire en distintas ciudades del mundo y niveles de polución.
# Catedra Programación II, 2C.
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


def filtrar_por_anio_y_suma(tabla: list[dict],anio:int,atributo:str)->dict[str:list[int,float]]:
    """
    Recibe una tabla, un año y un atributo y produce un diccionario de la forma {ciudad:[numero_de_entradas,suma_de_valores]}
    la misma es la que se usa para luego aplicar la funcion promedio
    """
    ciudades_filtradas = {}
    for fila in tabla:
        anio_fecha = fila["Timestamp"][0]
        ciudad = fila["City"]
        atributo_individual = fila[atributo]

        if anio_fecha == anio:
            if ciudad in ciudades_filtradas:
                ciudades_filtradas[ciudad][0] += 1
                ciudades_filtradas[ciudad][1] += atributo_individual
            else:
                ciudades_filtradas[ciudad] = [1,atributo_individual]

    return ciudades_filtradas


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
    ciudades_promedios = mayores_promedios(promedio(filtrar_por_anio_y_suma(tabla,anio,"Dust_ug_m3")))
            
    return ciudades_promedios


def fecha_str(fecha: tuple) -> str:
    '''
    Fecha(tupla) -> Fecha("Mes año")

    Dada una "fecha" de la tabla, devuelve el string con 
    el nombre del mes y año.
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

    Dado el "promedio de UV", devuelve el "color" como str en su
    forma Hexadesimal, según la siguiente forma:

    Verde: 0 <= prom_UV < 1
    Amarillo: 1 <= prom_UV < 2
    Naranja: 2 <= prom_UV < 3
    Rojo: 3 <= prom-UV < 4
    Violeta: 4 <= prom_UV

    (La escala de los colores no es la que se suele usar en general, se 
    modificó para que sea más visual el cambio de colores).
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
    Tabla Fecha("Mes año") -> dict[str:tuple]

    dada una tabla y una fecha dada como string de la forma "mes año, filtra ciudades segun el año y mes pasados 
    y devuelve un diccionario de la forma: {ciudad:(latitud,longitud,promedio_indice_uv)}.
    Es decir cada ciudad queda asociada a sus coordenadas y al promedio de indice uv durante el mes del año indicado
    '''
    ciudades_filtradas = {}
    ubicaciones = {}
    
    for fila in tabla:
        fecha_fila = fecha_str(fila["Timestamp"])
        ciudad = fila["City"]
        ind_uv = fila['UV_Index']
        latitud = fila["Latitude"]
        longitud = fila["Longitude"]

        if fecha == fecha_fila:

            if ciudad in ciudades_filtradas:
                ciudades_filtradas[ciudad][0] += 1
                ciudades_filtradas[ciudad][1] += ind_uv
            else:
                ciudades_filtradas[ciudad] = [1,ind_uv]
        
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
    Tabla fecha("Mes año") -> list[dict]

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
    ciudad_america('Tokyo') == False
    '''
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
    ciudades_promedios = mayores_promedios(promedio(filtrar_por_anio_y_suma(tabla_america,anio,"PM2_5_ug_m3")))
            
    return ciudades_promedios


def ejecutar_pregunta1(tabla: list[dict]):
    '''
    Produce los componentes de la pregunta 1 en la pagina
    '''

    st.title("¿Cuales fueron las 5 ciudades con mayor promedio de polvo en 2025?")
    st.table(pregunta_1(tabla, 2025))


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
        
    ubicaciones_promedios = filtrar_ubicacionesXmes(tabla, opcion)
        
    st.map(ubicaciones_promedios, latitude = "Latitude", longitude = "Longitude", color = "Color", size = 40000)


def filtrar_por_ubicación(tabla,lat_sup:int,lat_inf:int,long_inf:int,long_sup:int)-> dict[str:int]:
    '''
    Recibe una tabla y la filtra según latitud inferior y superior, y longitud inferior y superior.
    Produce un un diccionario de la forma {ciudad : cantidad de eventos catastroficos}
    '''
    tabla_filtrada={}
    for entrada in tabla:
        if lat_inf < entrada["Latitude"] and lat_sup > entrada["Latitude"] and long_inf < entrada["Longitude"] and long_sup > entrada["Longitude"]: #verifica si las coordenadas son correctas
            if entrada["City"] in tabla_filtrada:
                tabla_filtrada[entrada["City"]]+=entrada["Hazardous_Event"]
            else:
                tabla_filtrada[entrada["City"]] = entrada["Hazardous_Event"]
    return tabla_filtrada


def confirmar_datos(tabla,lat_sup:int,lat_inf:int,long_inf:int,long_sup:int):
    '''
    Esta función toma los valores de entrada del usuario de la pregunta 3, verifica que sean válidos y produce la tabla de valores. 
    '''
    if lat_inf>lat_sup or long_inf>long_sup:
        st.write("Valores inválidos.")
    else:
        st.table(mayores_promedios(filtrar_por_ubicación(tabla,lat_sup,lat_inf,long_inf,long_sup)))




def ejecutar_pregunta4(tabla):
    
   st.title("¿Qué 5 ciudades entre las latitudes X y longitudes X tuvieron mayor cantidad de días con catástrofes naturales en 2025?")
   st.write("Ingrese valores entre -90 y 90 para la latitud y entre -180 y 180 para la longitud. De manera que la latitud inferior sea menor a la latitud superor y la longitud inferior sea menor a la longitud superior.")
   latitud_inferior= st.slider("Latitud Inferior",-90,90)
   latitud_superior= st.slider("Latitud Superior",-90,90)
   longitud_inferior=st.slider("Longitud Inferior",-180,180)
   longitud_superior=st.slider("Longitud Superior",-180,180)
   def callback():
    return confirmar_datos(tabla, latitud_superior, latitud_inferior, longitud_inferior, longitud_superior)
   boton= st.button("Buscar",None,None, callback)


def ejecutar_pregunta3(tabla: list[dict]):
    '''
    Produce los componentes de la pregunta 3 en la pagina
    '''
    st.title("¿Cuáles son las 5 ciudades de América con mayor cantidad de PM2.5 en 2025?")

    dic= pregunta_3(tabla,2025)
    x=dic["ciudades"]
    y=dic["promedios"]
    bar_colors = ['tab:blue', 'tab:red', 'tab:orange']

    fig, ax = plt.subplots()
    ax.bar(x, y, color=bar_colors)

    ax.set_title("5 ciudades de América con mayor promedio de PM2.5 en 2025")
    ax.set_xlabel("ciudades")
    ax.set_ylabel("promedios")

    st.pyplot(fig)


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


def filtar_promedio_ciudades_por_fecha(tabla: list[dict], atributo: str, fecha: str) -> dict[str: float]:
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


def promedios_componentes_de_ciudades(tabla: list[dict], fecha: str) -> dict[list[float]]:
    '''
    tabla fecha -> {ciudad: [promedios]}

    Dada una tabla y una fecha de la forma "mes año", devuelve un diccionario cuyas claves son
    los nombres de las ciudades y sus valores son listas (ordenadas) de los promedios de
    las componentes del aire correspondientes a la misma en la fecha dada.
    '''
    dic = {}
    componentes = ["PM10_ug_m3", "PM2_5_ug_m3", "Carbon_Monoxide_ug_m3", "Nitrogen_Dioxide_ug_m3",
                   "Ozone_ug_m3", "Dust_ug_m3"]
    
    for componente in componentes:
        promedios_componente = filtar_promedio_ciudades_por_fecha(tabla,componente,fecha)

        for ciudad in promedios_componente:
            promedio = promedios_componente[ciudad]

            if ciudad in dic:
                dic[ciudad].append(promedio)
            else:
                dic[ciudad] = [promedio]
    
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


def main():
    #python -m streamlit run proyecto.py para ejecutar la aplicación
    tabla = procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")
    ejecutar_programa(tabla)


if __name__ == "__main__":
    main()