"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    with open('clusters_report.txt') as report:
        rows = report.readlines()
    rows = rows[4:]
    df = pd.DataFrame(columns=["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave","principales_palabras_clave"]) 
    for row in rows:
        if re.match('^ +[0-9]+ +', row):
            p_claves=""
            cluster, num_pc, porcen, *pc = row.split()
            pc.pop(0) 
            pc = ' '.join(pc) 
            p_claves += pc
            df.loc[cluster]=[int(cluster),int(num_pc),float(porcen.replace(',','.')),p_claves]
        elif re.match('^ +[a-z]', row):
            pc = row.split()
            pc = ' '.join(pc) 
            p_claves += ' ' + pc 
            df.at[cluster, 'principales_palabras_clave'] = p_claves
        
        elif re.match('^\n', row) or re.match('^ +$', row):
            df.at[cluster, 'principales_palabras_clave'] = df.at[cluster, 'principales_palabras_clave'].replace('.', '')
        
    df.reset_index(drop=True, inplace=True)

    return df
