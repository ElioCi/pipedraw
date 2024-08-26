import streamlit as st

import pandas as pd
import csv

# Titolo dell'applicazione
st.title('Inserimento Dati Caratteristici di Più Tratti di Condotta')

# Creazione di una lista per memorizzare i dati
if 'data' not in st.session_state:
    st.session_state['data'] = []

#lettura dati da file
diaList = []
with open('files/diametri.csv', newline='') as diameters:
    diameters_data = csv.reader(diameters)
    next(diameters_data) #salta la riga di testa
    for row in diameters_data:
        diaList.append(row[0])
with open('files/Dia_thk.csv') as file_thk:
    df = pd.read_csv(file_thk, delimiter = ";")   # lettura file e creazione dataFrame
with open('files/ExtDia.csv') as file_extDia:
    dfDia = pd.read_csv(file_extDia, delimiter = ";", index_col= 1)   # lettura file e creazione dataFrame e indicizzazione secondo colonna 1 (DN)

# Widget di input per inserire i dati
def diaSelected():
    return
def thkSelected():
    return

nome_tratto = st.text_input('Nome del Tratto')
lunghezza = st.number_input('Lunghezza (m)', min_value=0.0, step=0.1)
#diametro = st.number_input('Diametro (mm)', min_value=0.0, step=0.1)
diametro =st.selectbox ('Pipe ND [inches]', options=(diaList), on_change= diaSelected)
thkList = df[diametro].dropna()
spessore = st.selectbox("Pipe sect Thk [mm]", options=(thkList), on_change= thkSelected)

pressione = st.number_input('Pressione (bar)', min_value=0.0, step=0.1)
temperatura = st.number_input('Temperatura (°C)', min_value=0.0, step=0.1)

numlayers = st.number_input("no of insulation layers", min_value=0, max_value=3, step= 1)

condInsul =[]
insulThk = []
col1, col2, col3 = st.columns([1, 2, 2])
for i in range( numlayers):
    col1.write("Layer")
    col1.write(i+1)
    condInsul1 = col2.number_input(f"Insul therm cond [W/m°K] {i+1}", value= 0.040, step= 0.005, format="%0.3f")
    insulThk1 = col3.number_input(f"Insulation Thk [mm] {i+1}", value= 20, step= 5)
        
    condInsul.append(condInsul1)
    insulThk.append(insulThk1)    

# Pulsante per aggiungere i dati
if st.button('Aggiungi Tratto'):
    st.session_state['data'].append({
        'Nome Tratto': nome_tratto,
        'Lunghezza (m)': lunghezza,
        'Diametro (mm)': diametro,
        'Spessore (mm)': spessore,
        'Layers' : numlayers,
        'CondInsul': condInsul,
        'insulThk (mm)': insulThk,
        'Pressione (bar)': pressione,
        'Temperatura (°C)': temperatura
    })
    st.success('Tratto aggiunto con successo!')

# Visualizzazione dei dati inseriti
if st.session_state['data']:
    df = pd.DataFrame(st.session_state['data'])
    st.subheader('Dati dei Tratti di Condotta Inseriti')
    st.dataframe(df)

    df.to_csv("files/DatiPiping.csv")   # salva dati su DatiPiping      


