from proyecto import *

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

def test_ordenar_primeros_5():
    assert ordenar_primeros_5({'ciudades': ['Tokyo', 'Beijing', 'Mumbai', 'Mexico City', 'Moscow'], 'promedios': [1.0, 14.0, 41.0, 1.0, 0.0]}) == {'ciudades': [  'Mumbai','Beijing', 'Tokyo','Mexico City', 'Moscow'], 'promedios': [ 41.0, 14.0,1.0, 1.0, 0.0]}
    assert ordenar_primeros_5({'ciudades': ['Tokyo', 'Beijing', 'Mumbai', 'Mexico City', 'Moscow'], 'promedios': [40.0, 22.0, 32.0, 99.0, 36.0]}) == {'ciudades': [  'Mexico City','Tokyo', 'Moscow','Mumbai', 'Beijing'], 'promedios': [ 99.0, 40.0,36.0, 32.0, 22.0]}
    
def test_mayores_promedios():
    assert mayores_promedios({'Paris':30.1,'Tokyo':10.4,'Seoul':5.20,'Beijing':4.3,'Mumbai':10.6,'Bangkok':8.0,'Moscow':0.0}) == {'ciudades':['Paris','Mumbai','Tokyo','Bangkok','Seoul'],'promedios':[30.1,10.6,10.4,8.0,5.20]}
    assert mayores_promedios({'Paris':0.1,'Tokyo':0.4,'Seoul':5.20,'Beijing':6.3,'Mumbai':10.6,'Bangkok':8.0,'Moscow':0.0}) == {'ciudades':['Mumbai','Bangkok','Beijing','Seoul','Tokyo'],'promedios':[10.6,8.0,6.3,5.20,0.4]}

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
     {'ciudades': ['Delhi', 'Mumbai', 'Beijing', 'Tokyo', 'Mexico City'], 'promedios': [176.0, 41.0, 14.0, 1.0, 1.0]}

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
    assert filtrar_ubicacionesXmes([{'Timestamp': (2025, 12, 15, 2), 'City': 'Delhi', 'Latitude': 28.6139, 'Longitude': 77.209, 'PM10_ug_m3': 129.5, 'PM2_5_ug_m3': 36.9, 
     'Carbon_Monoxide_ug_m3': 635.0, 'Nitrogen_Dioxide_ug_m3': 16.5, 'Ozone_ug_m3': 89.0, 'Dust_ug_m3': 176.0, 'UV_Index': 0.0, 'European_AQI': 159, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 12, 7, 9), 'City': 'Beijing', 'Latitude': 39.9042, 'Longitude': 116.4074, 'PM10_ug_m3': 164.4, 'PM2_5_ug_m3': 154.6, 
     'Carbon_Monoxide_ug_m3': 1388.0, 'Nitrogen_Dioxide_ug_m3': 35.9, 'Ozone_ug_m3': 11.0, 'Dust_ug_m3': 14.0, 'UV_Index': 0.45, 'European_AQI': 177, 'Hazardous_Event': 1}, 
    {'Timestamp': (2025, 8, 11, 14), 'City': 'Mumbai', 'Latitude': 19.076, 'Longitude': 72.8777, 'PM10_ug_m3': 53.2, 'PM2_5_ug_m3': 26.5, 
     'Carbon_Monoxide_ug_m3': 170.0, 'Nitrogen_Dioxide_ug_m3': 4.6, 'Ozone_ug_m3': 101.0, 'Dust_ug_m3': 41.0, 'UV_Index': 7.05, 'European_AQI': 49, 'Hazardous_Event': 0},
    {'Timestamp': (2025, 11, 1, 22), 'City': 'Mexico City', 'Latitude': 19.4326, 'Longitude': -99.1332, 'PM10_ug_m3': 35.2, 'PM2_5_ug_m3': 34.8, 
    'Carbon_Monoxide_ug_m3': 546.0, 'Nitrogen_Dioxide_ug_m3': 68.6, 'Ozone_ug_m3': 37.0, 'Dust_ug_m3': 1.0, 'UV_Index': 0.0, 'European_AQI': 64, 'Hazardous_Event': 0}, 
    {'Timestamp': (2025, 9, 16, 6), 'City': 'Moscow', 'Latitude': 55.7558, 'Longitude': 37.6173, 'PM10_ug_m3': 47.1, 'PM2_5_ug_m3': 38.7, 
     'Carbon_Monoxide_ug_m3': 289.0, 'Nitrogen_Dioxide_ug_m3': 38.7, 'Ozone_ug_m3': 14.0, 'Dust_ug_m3': 0.0, 'UV_Index': 0.0, 'European_AQI': 63, 'Hazardous_Event': 0}],
     "Diciembre 2025") ==\
    [{'Latitude': 28.6139, 'Longitude': 77.209, 'Color': '#0DFF00C8'}, {'Latitude': 39.9042, 'Longitude': 116.4074, 'Color': '#0DFF00C8'}]