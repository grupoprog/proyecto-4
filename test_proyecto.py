from proyecto import *

tabla_completa=procesar_archivo("global_urban_smog_pm25_hourly_12k.csv")

tabla_de_prueba = [{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}]

def test_fechaAtupla():
    assert fechaAtupla("2025-10-02T06:00") == (2025,10,2,6)
    assert fechaAtupla("2025-09-30T23:00") == (2025,9,30,23)
    assert fechaAtupla("2026-02-08T01:00") == (2026,2,8,1)

def test_agregar_valor():
    assert agregar_valor({'Timestamp': '2026-02-07T06:00', 'City': 'Paris', 'Latitude': '48.8566', 'Longitude': '2.3522', 
    'PM10_ug_m3': '12.1', 'PM2_5_ug_m3': '6.3', 'Carbon_Monoxide_ug_m3': '178.0', 'Nitrogen_Dioxide_ug_m3': '10.5', 
    'Ozone_ug_m3': '50', 'Dust_ug_m3': '0', 'UV_Index': '0', 'European_AQI': '20', 'Hazardous_Event': '0'},
    "Timestamp", ['2026-02-07T06:00','Paris','48.8566','2.3522', '12.1', '6.3',  '178.0',  '10.5', '50', '0','0','20','0'],0)  == \
    {'Timestamp': (2026, 2, 7, 6), 'City': 'Paris', 'Latitude': '48.8566', 'Longitude': '2.3522', 
    'PM10_ug_m3': '12.1', 'PM2_5_ug_m3': '6.3', 'Carbon_Monoxide_ug_m3': '178.0', 'Nitrogen_Dioxide_ug_m3': '10.5', 
    'Ozone_ug_m3': '50', 'Dust_ug_m3': '0', 'UV_Index': '0', 'European_AQI': '20', 'Hazardous_Event': '0'}

def test_crear_fila():
    assert crear_fila(['Timestamp','City','Latitude','Longitude','PM10_ug_m3','PM2_5_ug_m3', 'Carbon_Monoxide_ug_m3', 'Nitrogen_Dioxide_ug_m3', 'Ozone_ug_m3', 'Dust_ug_m3', 'UV_Index', 'European_AQI', 'Hazardous_Event'],
    ['2026-02-07T06:00','Paris', '48.8566','2.3522', '12.1',  '6.3', '178.0','10.5', '50', '0',  '0',  '20','0'])==\
    {'Timestamp': (2026, 2, 7, 6), 'City': 'Paris', 'Latitude': 48.8566, 'Longitude': 2.3522, 
    'PM10_ug_m3': 12.1, 'PM2_5_ug_m3': 6.3, 'Carbon_Monoxide_ug_m3': 178.0, 'Nitrogen_Dioxide_ug_m3': 10.5, 
    'Ozone_ug_m3': 50.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 20, 'Hazardous_Event': 0}

def test_procesar_archivo():
    assert procesar_archivo("tabla_para_tests2.csv") ==\
    [{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0,
       'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 'PM2_5_ug_m3': 20.1, 
     'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2026, 2, 8, 1), 'City': 'Tehran', 'Latitude': 35.6892, 'Longitude': 51.389, 'PM10_ug_m3': 61.9, 'PM2_5_ug_m3': 59.3, 
      'Carbon_Monoxide_ug_m3': 4049.0, 'Nitrogen_Dioxide_ug_m3': 85.9, 'Ozone_ug_m3': 7.0, 'Dust_ug_m3': 5.0, 'UV_Index': 0.0, 'European_AQI': 107, 'Hazardous_Event': 1}, 
    {'Timestamp': (2026, 4, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}]

def test_promedio():
    assert promedio({'Paris': [10, 156.8], 'Tokyo':[4,16.4],'Beijing':[5,8.0], 'Seoul':[2,45.8] }) == {'Paris': 15.680000000000001, 'Tokyo':4.1,'Beijing':1.6, 'Seoul':22.9 }
    assert promedio({'Buenos Aires': [1, 200.8], 'Mumbai':[7,234.8],'New York':[3,128.9], 'Seoul':[8,460.8] }) == {'Buenos Aires': 200.8, 'Mumbai': 33.542857142857144, 'New York': 42.96666666666667, 'Seoul': 57.6}

def test_ordenar_primeros_5():
    assert ordenar_primeros_5({'Ciudades': ['Tokyo', 'Beijing', 'Mumbai', 'Mexico City', 'Moscow'], 'promedios': [1.0, 14.0, 41.0, 1.0, 0.0]},"promedios") == {'Ciudades': [  'Mumbai','Beijing', 'Tokyo','Mexico City', 'Moscow'], 'promedios': [ 41.0, 14.0,1.0, 1.0, 0.0]}
    assert ordenar_primeros_5({'Ciudades': ['Tokyo', 'Beijing', 'Mumbai', 'Mexico City', 'Moscow'], 'promedios': [40.0, 22.0, 32.0, 99.0, 36.0]},"promedios") == {'Ciudades': [  'Mexico City','Tokyo', 'Moscow','Mumbai', 'Beijing'], 'promedios': [ 99.0, 40.0,36.0, 32.0, 22.0]}
    
def test_mayores_valores():
    assert mayores_valores({'Paris':30.1,'Tokyo':10.4,'Seoul':5.20,'Beijing':4.3,'Mumbai':10.6,'Bangkok':8.0,'Moscow':0.0},"promedios") == {'Ciudades':['Paris','Mumbai','Tokyo','Bangkok','Seoul'],'promedios':[30.1,10.6,10.4,8.0,5.20]}
    assert mayores_valores({'Paris':0.1,'Tokyo':0.4,'Seoul':5.20,'Beijing':6.3,'Mumbai':10.6,'Bangkok':8.0,'Moscow':0.0},"promedios") == {'Ciudades':['Mumbai','Bangkok','Beijing','Seoul','Tokyo'],'promedios':[10.6,8.0,6.3,5.20,0.4]}

def test_contar_apariciones_y_sumar_elementos():
    assert contar_apariciones_y_sumar_elementos({'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 
    'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9,'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 
    'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1},'PM10_ug_m3',{},
    'Delhi',2025==2025) == {'Delhi': [1, 129.5]}
    assert contar_apariciones_y_sumar_elementos({'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 
    'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9,'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5,
     'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1},'PM10_ug_m3',
     {'Bogota': [2,19.17], 'Dhaka': [1,98.95], 'Riyadh': [3,1758.61],'Delhi':[6,2894.57]},'Delhi',2025==2025) == {'Bogota': [2, 19.17], 'Dhaka': [1, 98.95], 'Riyadh': [3, 1758.61], 'Delhi': [7, 3024.07]}



def test_filtrar_por_anio_y_suma():
    assert filtrar_por_anio_y_suma([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0,
       'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 'PM2_5_ug_m3': 20.1, 
     'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2026, 2, 8, 1), 'City': 'Tehran', 'Latitude': 35.6892, 'Longitude': 51.389, 'PM10_ug_m3': 61.9, 'PM2_5_ug_m3': 59.3, 
      'Carbon_Monoxide_ug_m3': 4049.0, 'Nitrogen_Dioxide_ug_m3': 85.9, 'Ozone_ug_m3': 7.0, 'Dust_ug_m3': 5.0, 'UV_Index': 0.0, 'European_AQI': 107, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 4, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}],2026,'PM2_5_ug_m3')==\
     {'Mexico City': [1, 25.0], 'Sao Paulo': [1, 7.5], 'Tehran': [1, 59.3]}

def test_pregunta_1():
    assert  pregunta_1([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0,
       'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 'PM2_5_ug_m3': 20.1, 
     'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2026, 2, 8, 1), 'City': 'Tehran', 'Latitude': 35.6892, 'Longitude': 51.389, 'PM10_ug_m3': 61.9, 'PM2_5_ug_m3': 59.3, 
      'Carbon_Monoxide_ug_m3': 4049.0, 'Nitrogen_Dioxide_ug_m3': 85.9, 'Ozone_ug_m3': 7.0, 'Dust_ug_m3': 5.0, 'UV_Index': 0.0, 'European_AQI': 107, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 4, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
     2025) ==\
     {'Ciudades': ['Delhi', 'Mumbai', 'Beijing', 'Tokyo', 'Mexico City'], 'Promedios': [176.0, 41.0, 14.0, 1.0, 1.0]}

def test_fecha_str():
    assert fecha_str((2025, 1, 10, 9)) == "Enero 2025"
    assert fecha_str((2025, 8, 2, 15)) == "Agosto 2025"
    assert fecha_str((2026, 5, 27, 18)) == "Mayo 2026"

def test_elegir_color():
    assert elegir_color(15.0) == "#C300FFC6"
    assert elegir_color(1.65) == "#FFFF00C8"
    assert elegir_color(0.0) == "#0DFF00C8"

def test_filtrar_ciudades():
    assert filtrar_ciudades([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 
    'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0, 'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5,
    'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 
    'PM2_5_ug_m3': 20.1, 'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0,
    'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 
     'PM2_5_ug_m3': 7.5, 'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 
     'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}],"Febrero 2026") == \
     {'Mexico City': (19.4326, -99.1332, 9.25), 'Tokyo': (35.6895, 139.6917, 0.0)}
    assert filtrar_ciudades([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 
    'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0, 'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5,
    'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 
    'PM2_5_ug_m3': 20.1, 'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0,
    'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 10, 9), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 7.5, 
     'PM2_5_ug_m3': 7.5, 'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 
     'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}],"Febrero 2026") ==\
    {'Mexico City': (19.4326, -99.1332, 7.825), 'Tokyo': (35.6895, 139.6917, 0.0)}

def test_filtrar_ubicacionesXmes():
    assert filtrar_ubicacionesXmes([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 
    'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0, 'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5,
    'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 
    'PM2_5_ug_m3': 20.1, 'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0,
    'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 10, 9), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 7.5, 
     'PM2_5_ug_m3': 7.5, 'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 
     'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}],"Febrero 2026") ==\
    [{'Latitude': 19.4326, 'Longitude': -99.1332, 'Color': '#C300FFC6'}, {'Latitude': 35.6895, 'Longitude': 139.6917, 'Color': '#0DFF00C8'}]

    assert filtrar_ubicacionesXmes(tabla_de_prueba,"Diciembre 2025") ==\
    [{'Latitude': 28.6139, 'Longitude': 77.209, 'Color': '#0DFF00C8'}, {'Latitude': 39.9042, 'Longitude': 116.4074, 'Color': '#0DFF00C8'}]

def test_ciudad_america():
    assert ciudad_america('Mexico City') == True
    assert ciudad_america('Tokyo') == False

def test_filtrar_ciudades_america():
    assert filtrar_ciudades_america([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0,
       'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 'PM2_5_ug_m3': 20.1, 
     'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}]) ==\
    [{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0, 
    'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 
    'Hazardous_Event': 0}, {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 
    'PM2_5_ug_m3': 7.5, 'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 
    'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}]
    assert  filtrar_ciudades_america([{'Timestamp': (2026, 2, 15, 13), 'City': 'Buenos Aires', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0,
       'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 30, 23), 'City': 'New York', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 'PM2_5_ug_m3': 20.1, 
     'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Lima', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2026, 2, 8, 1), 'City': 'Cairo', 'Latitude': 35.6892, 'Longitude': 51.389, 'PM10_ug_m3': 61.9, 'PM2_5_ug_m3': 59.3, 
      'Carbon_Monoxide_ug_m3': 4049.0, 'Nitrogen_Dioxide_ug_m3': 85.9, 'Ozone_ug_m3': 7.0, 'Dust_ug_m3': 5.0, 'UV_Index': 0.0, 'European_AQI': 107, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 4, 15, 2), 'City': 'Jakarta', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Paris', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}]) ==\
    [{'Timestamp': (2026, 2, 15, 13), 'City': 'Buenos Aires', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0,
       'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 30, 23), 'City': 'New York', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 'PM2_5_ug_m3': 20.1, 
     'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Lima', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}]

def test_pregunta_3():
    assert pregunta_3([{'Timestamp': (2026, 4, 18, 9), 'City': 'New York', 'Latitude': 40.7128, 'Longitude': -74.006, 'PM10_ug_m3': 14.0, 'PM2_5_ug_m3': 12.6, 
    'Carbon_Monoxide_ug_m3': 288.0, 'Nitrogen_Dioxide_ug_m3': 23.6, 'Ozone_ug_m3': 57.0, 'Dust_ug_m3': 2.0, 'UV_Index': 2.1, 'European_AQI': 23, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 18, 19), 'City': 'Tehran', 'Latitude': 35.6892, 'Longitude': 51.389, 'PM10_ug_m3': 110.6,  'PM2_5_ug_m3': 108.7, 
    'Carbon_Monoxide_ug_m3': 10165.0, 'Nitrogen_Dioxide_ug_m3': 109.5, 'Ozone_ug_m3': 0.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 76, 'Hazardous_Event': 0}, 
    {'Timestamp': (2026, 3, 3, 16), 'City': 'Buenos Aires', 'Latitude': -34.6037, 'Longitude': -58.3816, 'PM10_ug_m3': 10.4, 'PM2_5_ug_m3': 10.0, 
    'Carbon_Monoxide_ug_m3': 188.0, 'Nitrogen_Dioxide_ug_m3': 6.1, 'Ozone_ug_m3': 104.0, 'Dust_ug_m3': 0.0, 'UV_Index': 2.35, 'European_AQI': 43, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 10, 31, 21), 'City': 'Seoul', 'Latitude': 37.5665, 'Longitude': 126.978, 'PM10_ug_m3': 36.1, 'PM2_5_ug_m3': 32.7, 
    'Carbon_Monoxide_ug_m3': 466.0, 'Nitrogen_Dioxide_ug_m3': 61.6, 'Ozone_ug_m3': 23.0, 'Dust_ug_m3': 6.0, 'UV_Index': 0.0, 'European_AQI': 77, 'Hazardous_Event': 0}, 
    {'Timestamp': (2026, 1, 5, 21), 'City': 'Istanbul', 'Latitude': 41.0082, 'Longitude': 28.9784, 'PM10_ug_m3': 99.7, 'PM2_5_ug_m3': 70.1, 
    'Carbon_Monoxide_ug_m3': 693.0, 'Nitrogen_Dioxide_ug_m3': 69.4, 'Ozone_ug_m3': 2.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 36, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 6, 29, 17), 'City': 'Lahore', 'Latitude': 31.5204, 'Longitude': 74.3587, 'PM10_ug_m3': 94.3, 'PM2_5_ug_m3': 52.6, 
    'Carbon_Monoxide_ug_m3': 912.0, 'Nitrogen_Dioxide_ug_m3': 14.7, 'Ozone_ug_m3': 190.0, 'Dust_ug_m3': 83.0, 'UV_Index': 0.45, 'European_AQI': 87, 'Hazardous_Event': 0}, 
    {'Timestamp': (2026, 3, 4, 13), 'City': 'Riyadh', 'Latitude': 24.7136, 'Longitude': 46.6753, 'PM10_ug_m3': 2518.3, 'PM2_5_ug_m3': 221.7, 
    'Carbon_Monoxide_ug_m3': 202.0, 'Nitrogen_Dioxide_ug_m3': 11.1, 'Ozone_ug_m3': 116.0, 'Dust_ug_m3': 4774.0, 'UV_Index': 4.6, 'European_AQI': 592, 'Hazardous_Event': 1}, 
    {'Timestamp': (2026, 1, 3, 20), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 178.8, 'PM2_5_ug_m3': 170.4, 
    'Carbon_Monoxide_ug_m3': 1338.0, 'Nitrogen_Dioxide_ug_m3': 88.4, 'Ozone_ug_m3': 3.0, 'Dust_ug_m3': 15.0, 'UV_Index': 0.0, 'European_AQI': 116, 'Hazardous_Event': 1},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Lima', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0,
    'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5, 'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 'PM2_5_ug_m3': 20.1, 
     'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 'PM2_5_ug_m3': 7.5, 
     'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}],2026)==\
     {'Ciudades': ['New York', 'Buenos Aires', 'Lima', 'Mexico City', 'Sao Paulo'], 'Promedios': [12.6, 10.0, 7.5, 25.0, 7.5]}


def test_listar_por_atributo():
    assert listar_por_atributo([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 
    'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0, 'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5,
    'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 
    'PM2_5_ug_m3': 20.1, 'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0,
    'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 1, 10, 9), 'City': 'Sao Paulo', 'Latitude': -23.5505, 'Longitude': -46.6333, 'PM10_ug_m3': 7.5, 
    'PM2_5_ug_m3': 7.5, 'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 
    'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}], "City") == \
    ['Mexico City','Tokyo','Sao Paulo']
    assert listar_por_atributo([{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
     "Hazardous_Event") == [1,0]
    assert listar_por_atributo([{'Timestamp': (2026, 2, 15, 13), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 
    'PM10_ug_m3': 25.3, 'PM2_5_ug_m3': 25.0, 'Carbon_Monoxide_ug_m3': 271.0, 'Nitrogen_Dioxide_ug_m3': 4.5,
    'Ozone_ug_m3': 184.0, 'Dust_ug_m3': 0.0, 'UV_Index': 9.25, 'European_AQI': 70, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 30, 23), 'City': 'Tokyo', 'Latitude': 35.6895, 'Longitude': 139.6917, 'PM10_ug_m3': 23.5, 
    'PM2_5_ug_m3': 20.1, 'Carbon_Monoxide_ug_m3': 321.0, 'Nitrogen_Dioxide_ug_m3': 53.1, 'Ozone_ug_m3': 41.0, 'Dust_ug_m3': 1.0,
    'UV_Index': 0.0, 'European_AQI': 25, 'Hazardous_Event': 0},
    {'Timestamp': (2026, 2, 10, 9), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 7.5, 
     'PM2_5_ug_m3': 7.5, 'Carbon_Monoxide_ug_m3': 306.0, 'Nitrogen_Dioxide_ug_m3': 9.0, 'Ozone_ug_m3': 154.0, 'Dust_ug_m3': 0.0, 
     'UV_Index': 6.4, 'European_AQI': 64, 'Hazardous_Event': 0}], "City") == ["Mexico City", "Tokyo"]
    
def test_filtrar_promedio_ciudades_por_fecha():
    assert filtrar_promedio_ciudades_por_fecha([{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
    "PM10_ug_m3", "Diciembre 2025") == {"Delhi": 129.5, "Beijing": 164.4}
    assert filtrar_promedio_ciudades_por_fecha([{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 11, 14), 'City': 'Delhi', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 12, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
    "PM10_ug_m3", "Diciembre 2025") == {"Delhi": 91.35, "Beijing": 164.4, "Mexico City": 35.2}
    assert filtrar_promedio_ciudades_por_fecha([{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
    "Carbon_Monoxide_ug_m3", "Diciembre 2025") == {"Delhi": 635.0, "Beijing": 1388.0}

def test_aux():
    assert aux(filtrar_promedio_ciudades_por_fecha(tabla_completa,"PM10_ug_m3","Enero 2026"),'PM10_ug_m3',{})=={'Sao Paulo': [15.897297297297298], 'Mumbai': [61.11515151515152], 'Tehran': [63.86153846153846], 'Mexico City': [34.34791666666667], 
    'Bogota': [19.174193548387095], 'Dhaka': [98.95], 'Riyadh': [1758.6142857142854], 'Karachi': [49.90625000000001], 'Delhi': [120.66511627906974], 
    'Tokyo': [34.94642857142857], 'Johannesburg': [24.250000000000004], 'Buenos Aires': [8.3], 'Istanbul': [53.71794871794871], 
    'Jakarta': [51.46451612903226], 'Moscow': [84.3051282051282], 'Cairo': [91.87333333333332], 'Lahore': [137.5225806451613],
     'Lagos': [56.17948717948719], 'Dubai': [70.13666666666667], 'New York': [11.392592592592589], 'Lima': [35.12972972972973], 
     'Shanghai': [67.58181818181819], 'Paris': [22.856521739130432], 'Bangkok': [35.21470588235293], 'London': [13.811363636363636],
      'Beijing': [129.01935483870966], 'Los Angeles': [21.638888888888886], 'Seoul': [32.847368421052636], 'Chicago': [11.389999999999997]}
      
def test_promedios_componentes_de_ciudades():
    assert promedios_componentes_de_ciudades([{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
     "Diciembre 2025") == {"Delhi":[129.5,36.9,635.0,16.5,89.0,176.0], "Beijing":[164.4,154.6,1388.0,35.9,11.0,14.0]}
    assert promedios_componentes_de_ciudades([{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 11, 14), 'City': 'Delhi', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 12, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
     "Diciembre 2025") == {"Delhi":[91.35,31.7,402.5,10.55,95.0,108.5], "Beijing":[164.4,154.6,1388.0,35.9,11.0,14.0], "Mexico City":[35.2,34.8,546.0,68.6,37.0,1.0]}


def test_lat_long_validas():
    assert lat_long_validas(100,0,0,100,-5,500) == False
    assert lat_long_validas(100,0,0,100,50,20) == True

def test_filtrar_por_ubicacion():
    assert filtrar_por_ubicacion(tabla_de_prueba,90,-90,-180,180) == {'Delhi': 1, 'Beijing': 1, 'Mumbai': 0, 'Mexico City': 0, 'Moscow': 0}
    assert filtrar_por_ubicacion(tabla_de_prueba,-80,-90,170,180) == {}
    assert filtrar_por_ubicacion(tabla_de_prueba,21,19,71,73) == {'Mumbai': 0}




def test_promedios_monoxido_por_mes():
    assert promedios_monoxido_por_mes('Mexico City',tabla_completa) ==\
    [603.0, 645.3703703703703, 587.5714285714286, 642.2258064516129, 686.081081081081, 663.0909090909091, 660.5, 713.5454545454545, 
    662.7916666666666, 778.0666666666667, 499.07142857142856, 512.0370370370371, 537.1428571428571]
    assert  promedios_monoxido_por_mes('London',tabla_completa) ==\
    [141.75, 154.1, 152.45454545454547, 168.3548387096774, 156.05882352941177, 152.58064516129033, 176.8181818181818, 172.74193548387098, 
    213.5681818181818, 212.06060606060606, 214.96428571428572, 185.97222222222223, 157.08333333333334]


def test_pregunta_6():
    assert pregunta_6(tabla_completa) ==\
    {'Mexico City': [603.0, 645.3703703703703, 587.5714285714286, 642.2258064516129, 686.081081081081, 663.0909090909091, 660.5, 713.5454545454545,
     662.7916666666666, 778.0666666666667, 499.07142857142856, 512.0370370370371, 537.1428571428571], 
    'Bangkok': [871.75, 944.4242424242424, 1060.128205128205, 674.3666666666667, 1243.969696969697, 1084.5263157894738, 1344.2424242424242, 
     1172.4285714285713, 1140.764705882353, 743.4761904761905, 740.8095238095239, 520.4358974358975, 671.8095238095239], 
    'Dubai': [408.3, 449.4864864864865, 412.1714285714286, 388.14285714285717, 412.5882352941176, 481.1290322580645, 472.7674418604651, 
     406.41379310344826, 428.6666666666667, 511.4074074074074, 425.85185185185185, 492.7241379310345, 408.6060606060606], 
    'Dhaka': [322.9166666666667, 377.82758620689657, 378.8181818181818, 372.94117647058823, 402.09090909090907, 750.8918918918919,
    602.5, 731.1111111111111, 759.421052631579, 675.7586206896551, 484.6666666666667, 408.8333333333333, 598.1666666666666], 
    'New York': [204.92307692307693, 258.1, 235.2093023255814, 266.5405405405405, 278.1923076923077, 212.13333333333333, 339.037037037037, 
    299.52777777777777, 294.14814814814815, 408.2121212121212, 282.9512195121951, 224.59459459459458, 202.9655172413793], 
    'Lahore': [737.0, 623.3333333333334, 938.4761904761905, 657.1666666666666, 889.1351351351351, 1620.4642857142858, 2428.2894736842104, 
    3277.8214285714284, 2550.7096774193546, 1577.5277777777778, 828.7222222222222, 602.0416666666666, 649.7777777777778], 
    'Los Angeles': [228.75, 211.72413793103448, 217.8709677419355, 282.7317073170732, 328.94444444444446, 374.0571428571429, 425.3142857142857,
    572.2105263157895, 365.19444444444446, 362.4516129032258, 381.60869565217394, 269.8048780487805, 220.20833333333334], 
    'Sao Paulo': [260.3333333333333, 401.79411764705884, 346.025, 367.25, 297.74285714285713, 325.219512195122, 301.9230769230769, 282.04651162790697,
    299.94594594594594, 330.5, 384.3225806451613, 383.46153846153845, 366.7307692307692], 
    'Buenos Aires': [236.75, 399.64285714285717, 309.62857142857143, 240.56756756756758, 283.43243243243245, 202.625, 208.33333333333334,
    172.8846153846154, 145.39285714285714, 151.25, 179.17948717948718, 276.05555555555554, 257.3478260869565], 
    'London': [141.75, 154.1, 152.45454545454547, 168.3548387096774, 156.05882352941177, 152.58064516129033, 176.8181818181818,
    172.74193548387098, 213.5681818181818, 212.06060606060606, 214.96428571428572, 185.97222222222223, 157.08333333333334], 
    'Karachi': [241.625, 272.969696969697, 240.7058823529412, 399.39285714285717, 319.7, 608.6842105263158, 836.9090909090909,
    1065.057142857143, 921.0625, 786.4642857142857, 540.1951219512196, 386.25714285714287, 324.04545454545456], 
    'Delhi': [506.7142857142857, 546.3846153846154, 775.7931034482758, 638.34375, 538.5, 999.8571428571429, 1144.8181818181818, 
    1357.6666666666667, 1424.3488372093022, 1048.3720930232557, 664.6333333333333, 635.4871794871794, 458.5], 
    'Bogota': [767.0, 1052.4666666666667, 815.8928571428571, 1030.2, 984.1212121212121, 1045.9285714285713, 1073.5142857142857, 
    1114.7021276595744, 836.5806451612904, 1175.52, 1062.0, 1314.8, 728.68], 
    'Lagos': [438.6, 507.4594594594595, 393.10526315789474, 377.85714285714283, 429.5769230769231, 513.7727272727273, 528.4, 515.6842105263158,
     521.0512820512821, 487.28, 374.4347826086956, 449.5531914893617, 399.95454545454544], 
    'Paris': [182.14285714285714, 180.66666666666666, 184.97368421052633, 206.44444444444446, 198.57142857142858, 195.7741935483871,
    255.67567567567568, 253.10714285714286, 349.1304347826087, 244.94117647058823, 262.4318181818182, 244.73076923076923, 200.7391304347826],
    'Tokyo': [260.1111111111111, 331.52777777777777, 240.48, 306.8809523809524, 311.8863636363636, 306.02941176470586, 526.8108108108108,
    521.2903225806451, 419.9642857142857, 462.5128205128205, 360.9148936170213, 300.9375, 306.4193548387097], 
    'Riyadh': [203.8, 205.07142857142858, 223.93939393939394, 209.12121212121212, 285.14285714285717, 393.9655172413793, 465.90625, 299.3, 
    390.14285714285717, 337.3529411764706, 254.88095238095238, 260.4117647058824, 272.5], 
    'Chicago': [197.07692307692307, 253.09677419354838, 279.8, 251.02777777777777, 246.44444444444446, 218.4848484848485, 
    243.02702702702703, 264.8, 249.25, 301.8235294117647, 257.0, 205.07142857142858, 165.86111111111111], 
    'Beijing': [520.8181818181819, 634.5142857142857, 790.9375, 1087.8974358974358, 922.8108108108108, 1554.3939393939395, 2011.1,
    3236.891891891892, 2546.451612903226, 1956.40625, 1235.1304347826087, 688.78125, 633.3684210526316], 
    'Moscow': [248.3, 268.6, 317.6857142857143, 317.95348837209303, 268.0, 386.1666666666667, 442.3125, 633.775, 958.6666666666666, 
    639.8275862068965, 750.6078431372549, 372.6666666666667, 323.0571428571429], 
    'Johannesburg': [1071.4444444444443, 937.3181818181819, 1077.952380952381, 569.7567567567568, 365.25, 393.5882352941176, 404.56666666666666,
     372.1470588235294, 350.70588235294116, 276.06060606060606, 364.23333333333335, 366.72727272727275, 651.4814814814815], 
     'Tehran': [1384.3846153846155, 1303.5135135135135, 1200.6315789473683, 1650.5, 2414.676470588235, 3713.4102564102564, 5431.066666666667, 
     4449.1621621621625, 3915.846153846154, 2690.6666666666665, 3002.0689655172414, 1926.942857142857, 1540.2083333333333], 
     'Jakarta': [3682.1, 3359.090909090909, 2636.2580645161293, 2217.0555555555557, 2721.28125, 2890.1612903225805, 1588.076923076923,
    1539.5882352941176, 2468.1935483870966, 2082.1724137931033, 1834.1785714285713, 3877.1794871794873, 3423.8695652173915], 
    'Istanbul': [178.53846153846155, 170.3548387096774, 159.0681818181818, 167.37209302325581, 170.0, 214.94736842105263, 287.0232558139535,
    318.8888888888889, 423.94871794871796, 360.030303030303, 349.6, 271.0, 223.1875], 
    'Seoul': [361.5, 404.0833333333333, 292.225, 350.13157894736844, 513.1538461538462, 556.5135135135135, 646.8571428571429, 
    683.3030303030303, 713.5526315789474, 838.3076923076923, 739.3055555555555, 478.9428571428571, 344.125], 
    'Lima': [489.75, 625.5111111111111, 535.6585365853658, 529.7647058823529, 518.0227272727273, 454.36842105263156, 466.2368421052632,
    283.3703703703704, 488.5135135135135, 625.9117647058823, 627.5744680851063, 657.6764705882352, 470.4347826086956],
    'Cairo': [173.8181818181818, 196.27777777777777, 207.09677419354838, 192.4102564102564, 213.6153846153846, 221.82857142857142, 
    335.85714285714283, 309.8857142857143, 476.8666666666667, 343.2631578947368, 270.55, 227.07894736842104, 203.19230769230768], 
    'Shanghai': [796.7, 1113.3225806451612, 694.7105263157895, 1179.225, 1456.1515151515152, 1070.0, 2241.9333333333334, 2749.823529411765, 
    2103.121212121212, 1960.9583333333333, 875.1923076923077, 1546.057142857143, 519.0], 
    'Mumbai': [387.3333333333333, 217.66666666666666, 203.5, 262.9714285714286, 358.90625, 487.7037037037037, 614.219512195122,
    595.5882352941177, 715.4848484848485, 705.0540540540541, 455.7837837837838, 359.3076923076923, 243.0]}


def test_coordenadas_validas():
    assert coordenadas_validas(12.2,7,-55,13) == False
    assert coordenadas_validas(55,-1.3,125,120) == True
    assert coordenadas_validas(0,0,0,0) == False