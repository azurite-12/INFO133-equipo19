import csv
#SENTENCIAS 1, 2, 13 y 14
tasa_total=[]
comunas_por_region=[]
tasa_individual=[]
comuna_seg=[]
region_seg=[]

for i in range(0,16,1):
    tasa_total.append(0)
    comunas_por_region.append(0)
with open('TablaSeguridad.csv', encoding='utf8') as File:  
    reader = csv.reader(File)
    bandera=False
    for row in reader:
        if bandera:
            r=int(row[5])-1
            tasa_total[r]=tasa_total[r]+float(row[2])
            comunas_por_region[r]=comunas_por_region[r]+1
            tasa_individual.append(float(row[2]))
            comuna_seg.append(row[1])
            region_seg.append(row[5])
        else:
            bandera=True#Salta la linea de encabezados
            
max_seguridad=tasa_total[0]
mas_segura=1
min_seguridad=0
menos_segura=0
CMS=[]

for j in range(0,16,1):#Responde 1 y 2
    tasa_total[j]=tasa_total[j]/comunas_por_region[j]
    if tasa_total[j]<max_seguridad:
        max_seguridad=tasa_total[j]
        mas_segura=j+1
    if tasa_total[j]>min_seguridad:
        min_seguridad=tasa_total[j]
        menos_segura=j+1
    CMS.append(-1)
    
for k in range(0,len(tasa_individual),1):#Responde 13
    L=int(region_seg[k])-1
    if (CMS[L]<0)or(tasa_individual[k])>(tasa_individual[CMS[L]]):
        CMS[L]=k
        
print("1) La region mas segura es la "+str(mas_segura)+"a con tasa promedio "+
      str(max_seguridad)+".\n2) La region menos segura es la "+str(menos_segura)+
      "a con tasa promedio "+str(min_seguridad)+".")

for i in range(1, len(tasa_individual)):#Responde 14 con InsertionSort
        ti = tasa_individual[i]
        cs = comuna_seg[i]
        rs = region_seg[i]
        z = i-1
        while z >= 0 and ti > tasa_individual[z] : 
                ti[z+1] = tasa_individual[z]
                comuna_seg[z+1] = comuna_seg[z]
                R_comuna[z+1] = R_comuna[z]
                z -= 1
        tasa_individual[z+1] = ti
        comuna_seg[z+1] = cs
        region_seg[z+1] = rs

#SENTENCIAS 3, 4 Y 11
IDH=[]
N_comuna=[]
R_comuna=[]
Regiones=[]
IDH_R=[]
CPR=[]
IDH_Max=[]
Comuna_Max=[]

with open('tablaidh_.csv',encoding='utf8') as Archivo:
    reader=csv.reader(Archivo, quoting=csv.QUOTE_MINIMAL)
    test=False
    for row in reader:
        if test:
            val=0.0
            if row[8]!="":
                row[8]=row[8].replace(',','.')
                val=float(row[8])
            IDH.append(val)
            N_comuna.append(row[1])
            R_comuna.append(row[4])
            if row[4] not in Regiones:
                Regiones.append(row[4])
                IDH_R.append(0.0)
                CPR.append(0.0)
                IDH_Max.append(0.0)
                Comuna_Max.append('')
        else:
            test=True#Salta la linea vacia inicial

for i in range(0,len(IDH),1):#Responde la 11
    j=0
    while R_comuna[i]!=Regiones[j]:
        j=j+1
    IDH_R[j]=IDH_R[j]+IDH[i]
    CPR[j]=CPR[j]+1.0
    if IDH[i]>IDH_Max[j]:
        IDH_Max[j]=IDH[i]
        Comuna_Max[j]=N_comuna[i]
        
Id_menor_IDH=0
Id_mayor_IDH=0
IDH_R[0]=IDH_R[0]/CPR[0]

for k in range(1,len(Regiones),1):#Responde 3 y 4
    IDH_R[k]=IDH_R[k]/CPR[k]
    if IDH_R[k]>IDH_R[Id_mayor_IDH]:
        Id_mayor_IDH=k
    if IDH_R[k]<IDH_R[Id_menor_IDH]:
        Id_menor_IDH=k

print("3) La region con mayor IDH promedio es "+Regiones[Id_mayor_IDH]+" con IDH = "+
      str(IDH_R[Id_mayor_IDH])+".\n4) La de menor IDH promedio es "+Regiones[Id_menor_IDH]+
      " con IDH = "+str(IDH_R[Id_menor_IDH])+".\n11)Las comunas con mayor IDH por region son:")
for i in range(0,len(Regiones),1):
    print(" - "+Comuna_Max[i]+" de "+Regiones[i]+", con IDH = "+str(IDH_Max[i]))
    
#SENTENCIA 12
for i in range(1, len(IDH)):#Se uso InsertionSort de nuevo
        idehache = IDH[i]
        noidh = N_comuna[i]
        reidh = R_comuna[i]
        w = i-1
        while w >= 0 and idehache > IDH[w] : 
                IDH[w+1] = IDH[w]
                N_comuna[w+1] = N_comuna[w]
                R_comuna[w+1] = R_comuna[w]
                w -= 1
        IDH[w+1] = idehache
        N_comuna[w+1] = noidh
        R_comuna[w+1] = reidh
        
print("12) La lista de comunas ordenadas segun su IDH en forma descendente es:")
for i in range(0, len(IDH)):
    print(" - "+N_comuna[i]+": "+str(IDH[i]))
    
print("13) Las comunas menos seguras por region son:")
for i in range(0,len(CMS),1):
    cmsi=CMS[i]
    print(" - "+comuna_seg[cmsi]+" de la "+region_seg[cmsi]+"a region con tasa de "
          +str(tasa_individual[cmsi]))
    
print("14) Lista de comunas segun tasa de seguridad mas su region:")
for j in range(0, len(tasa_individual), 1):
    print(" - "+str(j+1)+".- "+comuna_seg[j]+" de la "+region_seg[j]+"a region, con tasa de "
          +str(tasa_individual[j])+" cada cien mil habitantes.")
