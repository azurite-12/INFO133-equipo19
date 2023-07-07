import pandas as pd
import os
import glob

path = r'C:\Users\diego\.vscode\INFO133_2023\INFO133-equipo19\Parte B\Datos\pob'
archivos = glob.glob(os.path.join(path , "*.csv"))

li = []
for nombreArchivo in archivos:
    df = pd.read_csv(nombreArchivo, index_col=None, header=0)
    li.append(df)

bigFrame = pd.concat(li, axis=0, ignore_index=True)

bigFrame['Igualdad Laboral'] = bigFrame['Hombres Ocupados'] - bigFrame['Mujeres Ocupadas']

#SENTENCIA 9. Se muestra de orden descendiente las comunas con mayor igualdad laboral. Si es positivo, hay más hombres que mujerees trabajando.
print(bigFrame.sort_values(by='Igualdad Laboral', ascending=True))

#SENTENCIA 10. Se muestra de orden descendiente las comunas con menor igualdad laboral. Si es positivo, hay más hombres que mujerees trabajando.
print(bigFrame.sort_values(by='Igualdad Laboral', ascending=False))
