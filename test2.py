import streamlit as st
import pandas as pd
import csv
import ast

st.title("Lettura dati memorizzati su file e calcolo")

#Lettura dati
with open('files/DatiPiping.csv') as file_input:
        df = pd.read_csv(file_input)   # lettura file e creazione
        df.drop(df.columns[df.columns.str.contains('unnamed', case= False)], axis=1, inplace= True)

rows = df.shape[0]

#print("rows=", rows)
variabili = {}
for i, row in df.iterrows():
    variabili[f'riga_{i+1}'] = row.to_dict()

# Visualizza le variabili in Streamlit
st.write("I record del DataFrame salvati in variabili:")
for key, value in variabili.items():
    st.write(f"{key}: {value}")
    

valore11 = variabili['riga_1']['Nome Tratto']
valore12 = variabili['riga_1']['Lunghezza (m)']
numLayers = variabili['riga_1']['Layers']

riga_1 = variabili['riga_1']

condinsul_str =  riga_1['CondInsul']
condinsul_list = ast.literal_eval(condinsul_str)

# Recupera i valori dei vari strati
condinsul_dict = {}
for i in range(numLayers):
    #f'condinsul_{i}' = condinsul_list[i-1]
    condinsul_dict[f'condinsul_{i}'] = condinsul_list[i]



print("Nome tratto =", valore11)
print("Lunghezza =", valore12)

for i in range(numLayers):
    print("i , CondInsul =", i, condinsul_dict[f'condinsul_{i}'])

st.write(df)