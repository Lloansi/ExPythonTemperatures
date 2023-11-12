import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_1 = []
data_2 = []
data_3 = []

ruta_1 = "Numpy/MeteoCat_Metadades.csv"
ruta_2 = "Numpy/2022_MeteoCat_Detall_Estacions.csv"
ruta_3 = "Numpy/2020_MeteoCat_Estacions.csv"


def read_csv(rute, num):
    data = []
    aux = 0
   # Abre el archivo CSV en modo lectura
    with open(rute, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        for fila in lector_csv:
            data.append(fila)
        aux =+ 1

    match num:
        case 1:
            data_1.extend(data)
        case 2:
            data_2.extend(data)
        case 3:
            data_3.extend(data)

    #recorrer_csv(lector_csv)

def recorrer_csv(lector_csv):
    # Itera a través de cada fila en el archivo CSV
    for fila in lector_csv:
        # Accede a los elementos individuales de cada fila
        for elemento in fila:
            print(elemento, end=' ')
        print()  # Imprime una línea en blanco entre filas
    
def array_to_ndarray(list):
    array_numpy = np.array(list)
    return array_numpy

#Lectura dels 3 documents csv
#Document 1
#read_csv(ruta_1,1)
#Document 2
read_csv(ruta_2,2)
#Document 3
#read_csv(ruta_3,3)

#Pasem la informació extreta de la lectura a ndarray's
# Info a lista | Document 1
#array_numpy_1 = array_to_ndarray(data_1)
# Info a lista | Document 2
array_numpy_2 = array_to_ndarray(data_2)
# Info a lista | Document 3
#array_numpy_3 = array_to_ndarray(data_3)

#Eliminem els primers valors, que no son númerics de les arrays
#new_nparrays_1 = array_numpy_1[1:]
new_nparrays_2 = array_numpy_2[1:]
#new_nparrays_3 = array_numpy_3[1:]

# Imprimim l'array del document 1
#print(new_nparrays_1)
# Imprimim l'array del document 2
print(new_nparrays_2)
# Imprimim l'array del document 3
#print(new_nparrays_3)