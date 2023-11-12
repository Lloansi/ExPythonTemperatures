import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random as rnd

#Variables
ruta_csv = "Numpy/2022_MeteoCat_Detall_Estacions.csv"
names_estacions = []
plt.ylabel("Graus")
plt.suptitle("Temperatures Febrer")
avg_D5_per_day = []
avg_X2_per_day = []
avg_X4_per_day = []
avg_X8_per_day = []

labels = ['Plou', 'No Plou']
colores = ['lightgreen', 'lightcoral']

#DataFrame de les dades
df = pd.read_csv(ruta_csv)

def rain_filter(df):
    # ------------------- FILTRAR PER ACRONIM DE DADA --------------------

    # Creem una serie per filtar segons el acronim de les dades, en el qual busquem només les dades de mitjana de temperatura (TM), per recuperar les dades d'aquesta columna
    acronim_serie = df["ACRÒNIM"]
    filter_by_acronim = acronim_serie == "PPT"

    #Dades amb el filtre aplicat
    filtered_by_acronim = df[(acronim_serie == "PPT")]

    return filter_by_acronim

def date_filter(df):
    # --------------------- FILTRAR PER TEMPERATURA ---------------------

    # Creem una serie per filtrar només les dades de la columna "DATA_LECTURA", per recuperar les dades d'aquesta columna
    date_serie = df["DATA_LECTURA"]
    # Modifiquem el format, per poder tractar la informació com el que és, DATES.
    format_date_data = pd.to_datetime(date_serie)

    #Dates del principi i final del mes de febrer
    start_february = "2022-02-01"
    end_february = "2022-02-28"

    #Condicions per saber si pertany a febrer
    filter_start_february = format_date_data >= start_february
    filter_end_february = format_date_data <= end_february

    filter_february = filter_start_february & filter_end_february

    # Filtre per les dades de febrer (veure si pertany aquestes dates) , observem si es més gran que el primer dia de febrer o es més petit que el últim dia de febrer i si pertany entre aquest aquests valors, guardem tots els valors de la fila
    # Dades amb el filtre aplicat
    filtered_by_date = df[(filter_start_february & filter_end_february)]

    return filter_february

def type_filter(df):
    # ------------------- FILTRAR PER ACRONIM DE DADA --------------------

    # Creem una serie per filtar segons el acronim de les dades, en el qual busquem només les dades de mitjana de temperatura (TM), per recuperar les dades d'aquesta columna
    acronim_serie = df["ACRÒNIM"]
    filter_by_acronim = acronim_serie == "TM"

    #Dades amb el filtre aplicat
    filtered_by_acronim = df[(acronim_serie == "TM")]

    return filter_by_acronim

def estacio_filter(df):
    # ------------------- FILTRAR PER ESTACIO DE DADA --------------------

    #Creem la serie del codi de la estació, per recuperar les dades d'aquesta columna
    estacio = df["CODI_ESTACIO"]
    #Eliminem duplicats
    estacio.drop_duplicates(inplace=True)

    for est in estacio:
        names_estacions.append(est)

    codi_serie = df["CODI_ESTACIO"]

    filter_by_codi_D5 = codi_serie == "D5"
    filter_by_codi_X2 = codi_serie == "X2"
    filter_by_codi_X4 = codi_serie == "X4"
    filter_by_codi_X8 = codi_serie == "X8"

    #Dades amb el filtre aplicat
    filtered_by_codi = df[(codi_serie == "D5")]

    return filter_by_codi_D5, filter_by_codi_X2, filter_by_codi_X4, filter_by_codi_X8

def graph_all():
    filtered_by_date_acronim_estacioD5['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='blue', linestyle='-', marker = '.', linewidth=1, kind='line')
    filtered_by_date_acronim_estacioX2['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='red', linestyle='-', marker = '.', linewidth=1, kind='line')
    filtered_by_date_acronim_estacioX4['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='orange', linestyle='-', marker = '.', linewidth=1, kind='line')
    filtered_by_date_acronim_estacioX8['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='green', linestyle='-', marker = '.', linewidth=1, kind='line')
    plt.title("Temperatura")
    plt.grid(True)
    plt.legend()
    plt.savefig('AllDataFebruary.png')

def graph_D5():
    plt.subplot(1, 4, 1)  # 1 fila, 3 columnas, ubicación 1
    filtered_by_date_acronim_estacioD5['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='blue', linestyle='-', marker = '.', linewidth=1, kind='line')
    plt.title("Temperatura Estació 'D5'")
    plt.grid(True)
    plt.legend()

def graph_X2():
    plt.subplot(1, 4, 2)  # 1 fila, 3 columnas, ubicación 1
    filtered_by_date_acronim_estacioX2['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='red', linestyle='-', marker = '.', linewidth=1, kind='line')
    plt.title("Temperatura Estació 'X2'")
    plt.grid(True)
    plt.legend()

def graph_X4():
    plt.subplot(1, 4, 3)  # 1 fila, 3 columnas, ubicación 1
    filtered_by_date_acronim_estacioX4['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='orange', linestyle='-', marker = '.', linewidth=1, kind='line')
    plt.title("Temperatura Estació 'X4'")
    plt.grid(True)
    plt.legend()

def graph_X8():
    plt.subplot(1, 4, 4)  # 1 fila, 3 columnas, ubicación 1
    filtered_by_date_acronim_estacioX8['VALOR'].plot(x='DATA_LECTURA', y='VALOR', label='Temperatura', color='green', linestyle='-', marker = '.', linewidth=1, kind='line')
    plt.title("Temperatura Estació 'X8'")
    plt.grid(True)
    plt.legend()


#Agrupem la info de cada estació
def group_data_per_day_D5(filtered_by_date_acronim_estacioD5):

    # Agrupem la info per la data
    grouped_data_D5 = filtered_by_date_acronim_estacioD5.groupby('DATA_LECTURA')

    # Creem una llista buida
    data_per_day_D5 = []

    for date, group in grouped_data_D5:
        # Extreiem la info per cada dia
        data = group['VALOR'].values
        data_per_day_D5.extend(data)
    return data_per_day_D5

def group_data_per_day_X2(filtered_by_date_acronim_estacioX2):
    # Agrupem la info per la data
    grouped_data_X2 = filtered_by_date_acronim_estacioX2.groupby('DATA_LECTURA')

    # Creem una llista buida
    data_per_day_X2 = []

    for date, group in grouped_data_X2:
        # Extreiem la info per cada dia
        data = group['VALOR'].values
        data_per_day_X2.extend(data)
    return data_per_day_X2

def group_data_per_day_X4(filtered_by_date_acronim_estacioX4):
    # Agrupem la info per la data
    grouped_data_X4 = filtered_by_date_acronim_estacioX4.groupby('DATA_LECTURA')

    # Creem una llista buida
    data_per_day_X4 = []

    for date, group in grouped_data_X4:
        # Extreiem la info per cada dia
        data = group['VALOR'].values
        data_per_day_X4.extend(data)
    return data_per_day_X4

def group_data_per_day_X8(filtered_by_date_acronim_estacioX8):
    # Agrupem la info per la data
    grouped_data_X8 = filtered_by_date_acronim_estacioX8.groupby('DATA_LECTURA')

    # Creem una llista buida
    data_per_day_X8 = []

    for date, group in grouped_data_X8:
        # Extreiem la info per cada dia
        data = group['VALOR'].values
        data_per_day_X8.extend(data)
    return data_per_day_X8

# --------------------------------------------------- EX3 ---------------------------------------------------

#Filtres
filter_rain = rain_filter(df)
filter_february = date_filter(df)
filter_acronim = type_filter(df)
filter_code_D5, filter_code_X2, filter_code_X4, filter_code_X8 = estacio_filter(df)

#Ara utilitzem els filtres d'abans extrets de les funcions
filtered_by_date_acronim_estacioD5 = df[(filter_acronim) & (filter_february) & (filter_code_D5)]
filtered_by_date_acronim_estacioX2 = df[(filter_acronim) & (filter_february) & (filter_code_X2)]
filtered_by_date_acronim_estacioX4 = df[(filter_acronim) & (filter_february) & (filter_code_X4)]
filtered_by_date_acronim_estacioX8 = df[(filter_acronim) & (filter_february) & (filter_code_X8)]
filtered_all_february = df[(filter_acronim) & (filter_february)]


# --------------------------------------------------- EX4 ---------------------------------------------------

#EX 4.1
#Plot
graph_all()

#Subplots
plt.figure(figsize=(20, 10))
graph_D5()
graph_X2()
graph_X4()
graph_X8()
plt.savefig('EstacionsDataFebruary.png')

#Info de cada estació
avg_D5_per_day = group_data_per_day_D5(filtered_by_date_acronim_estacioD5)
avg_X2_per_day = group_data_per_day_X2(filtered_by_date_acronim_estacioX2)
avg_X4_per_day = group_data_per_day_X4(filtered_by_date_acronim_estacioX4)
avg_X8_per_day = group_data_per_day_X8(filtered_by_date_acronim_estacioX8)


# Combinem totes les dades extretes
mixed_list_all_estacions = zip(avg_D5_per_day, avg_X2_per_day, avg_X4_per_day, avg_X8_per_day)

# Calculem cada mitjana de valors de cada registre per separat
avg_estacio = [sum(values) / len(values) for values in mixed_list_all_estacions]

# Ara escollim els valors random de les mitjes
rnd_choice_each_estacio = [rnd.choice(avg_estacio) + rnd.random() for _ in range(len(avg_estacio))]

plt.figure()
plt.hist(rnd_choice_each_estacio , label='Temperatura', color="orange", bins=5 , edgecolor='red', alpha = 0.8)
plt.title("Temperatura Mitja Febrer")
plt.xlabel("Temperatura")
plt.ylabel("Quantitat")
plt.grid(True)
plt.legend()
plt.xlim(-10,25)
plt.xticks(np.arange(0, 20, 2))
plt.savefig('AvgDataFebrurary.png')


def predict_rain_february_2023(df):

    february_days = 28

    # Filtres
    filter_rain = rain_filter(df)
    filter_february = date_filter(df)
    filtered_february_rain = df[(filter_february) & (filter_rain)]

    # Comprobem si plou o no, utilitzant booleans, llavors amb el metodo mean , fem les mitjanes entre aquest TRUE (1) i FALSE (0), donanse la proporció del que ha plogut sobre el total de dies
    arr_rain_or_not = np.mean(filtered_february_rain['VALOR'] > 0)

    # Ara , aleatoriament calculem la probabilitat de que un dia sigui true (plou), false (no plou) i ho guardem a una array. El parametre "p" Representa la probabilitat de que sigui Cert (plou), i 1 - prob_lluvia_2022 representa la probabilitat de que sigui Fals (no plou).
    arr_rain_days_booleans = np.random.choice([True, False], size= february_days, p=[arr_rain_or_not, 1 - arr_rain_or_not])

    return arr_rain_days_booleans


prediction_rainning = predict_rain_february_2023(df)

# Com que prediction_rainning és una sèrie de valors booleans (True o False), osigui 0 i 1, la suma comptara quants elements són True (ja que es 1 i false es 0) es a dir, que plourà.
yes_raing_days = np.sum(prediction_rainning)

# Restar sum_rainning_days d'aquesta longitud ens donarà la quantitat de dies en que no va ploure (False).
no_rain_day = len(prediction_rainning) - yes_raing_days

days_have_raing_or_not = [yes_raing_days, no_rain_day]


plt.figure()
plt.subplot(1, 2, 1)

# Gràfic quesitos
plt.pie(days_have_raing_or_not, labels=labels, colors=colores, autopct='%1.1f%%', startangle=90)
plt.title("Predicció plujes 2023")

# Gràfic barres
plt.subplot(1, 2, 2)
plt.barh(labels, days_have_raing_or_not, color=colores)
plt.title("Predicció plujes 2023")

plt.savefig("Predictions.png")

plt.show()