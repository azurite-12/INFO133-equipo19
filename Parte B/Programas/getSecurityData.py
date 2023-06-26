import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

basepath="C:/Users/emper/Documents/BD"
archivo=basepath+"/pazciudadanacl_exportacion_14062023115901.xlsx"

df_com=pd.read_excel(archivo,sheet_name="Fundación Paz Ciudadana")
df_com.head()

#regiones=df_com.groupby(["Región"]).sum()
comunal=df_com[["Comuna","Tasa cada 100 Mil"]]
comunal.plot(kind="bar")
plt.show()
