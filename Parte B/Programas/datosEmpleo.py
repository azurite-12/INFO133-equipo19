import pandas as pd
import os
import glob

#SENTENCIA 5
df = pd.read_csv(r"C:\Users\diego\.vscode\INFO133_2023\INFO133-equipo19\Parte B\Datos\pob\14losrios.csv")

personasOrdenadas = df.sort_values(by='Población en Edad de Trabajar', ascending=True)
print(personasOrdenadas)


#SENTENCIA 7
path = r'C:\Users\diego\.vscode\INFO133_2023\INFO133-equipo19\Parte B\Datos\pob'
archivos = glob.glob(os.path.join(path , "*.csv"))

li = []
for nombreArchivo in archivos:
    df = pd.read_csv(nombreArchivo, index_col=None, header=0)
    li.append(df)

bigFrame = pd.concat(li, axis=0, ignore_index=True)

comunasOrdenadas = bigFrame.sort_values(by='Personas Desocupadas', ascending=False)
print(comunasOrdenadas)


#SENTENCIA 6
print("comuna con más desempleo: ", comunasOrdenadas.iat[1,0])


#SENTENCIA 8
comOrdenadasPob = bigFrame.sort_values(by='Población Total', ascending=False)
print(comOrdenadasPob)