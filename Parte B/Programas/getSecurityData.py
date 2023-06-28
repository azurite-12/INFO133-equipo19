import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

directorioActual = os.path.dirname(os.path.abspath(__file__))
rel_pat1 = '../Datos/pazciudadanacl_exportacion_14062023115901.xlsx'
archivo = os.path.join(directorioActual, rel_pat1)
#basepath='../Datos'
#archivo=basepath+'/pazciudadanacl_exportacion_14062023115901.xlsx'

df_com=pd.read_excel(archivo,sheet_name="Fundación Paz Ciudadana")
df_com.head()
df_com.to_csv('./TablaSeguridad.csv', index = None, header = True)

#regiones=df_com.groupby(["Región"]).sum()
comunal=df_com[["Comuna","Tasa cada 100 Mil"]]
comunal.plot(kind="bar")
plt.show()