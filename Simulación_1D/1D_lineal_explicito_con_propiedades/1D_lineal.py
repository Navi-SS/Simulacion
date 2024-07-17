from datos import *
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

columnas=['Celda1','Celda2','Celda3','Celda4','Celda5']
presiones=pd.DataFrame(columns=columnas)
presiones.loc[0]=P0[1:-1]
n=len(dx)

#Se calcula área y volumen
Ax=[dz[i]*dy[i] for i in range(n)]
Vb=[dx[i]*dz[i]*dy[i] for i in range(n)]

#Formamos la matriz solución "A"
c2,c5,gt,tiempo=np.array([]),np.array([]),np.array([]),[0]
for i in range(1,n-1):
	try:
		c2=np.append(c2,(2*Ax[i]*kx[i]*Ax[i-1]*kx[i-1])/(Ax[i]*kx[i]*dx[i-1]+Ax[i-1]*kx[i-1]*dx[i])*(Bc/(Bo[i]*vis)))
		c5=np.append(c5,(2*Ax[i]*kx[i]*Ax[i+1]*kx[i+1])/(Ax[i]*kx[i]*dx[i+1]+Ax[i+1]*kx[i+1]*dx[i])*(Bc/(Bo[i]*vis)))
		gt=np.append(gt,(Ac*B*dt)/(Vb[i]*poro[i]*Co[i]))
	except:
		pass
c2=np.nan_to_num(c2)
c5=np.nan_to_num(c5)

P1=P0
for t in range(dt,tf+1,dt):
	tiempo.append(t)
	for i in range(1,n-1):
		P1[i]=P0[i]+gt[i-1]*(q[i]+c5[i-1]*(P0[i+1]-P0[i])-c2[i-1]*(P0[i]-P0[i-1]))
	P0=P1
	presiones.loc[t/dt]=P0[1:-1]
#presiones['Time'] = tiempo
var1=sorted(columnas*len(tiempo))
df=pd.DataFrame(columns=['Presion','Celdas','Tiempo'])
df['Presion']=presiones.to_numpy().flatten(order='F')
df['Celdas']=sorted(columnas*len(tiempo))
df['Tiempo']=tiempo*len(columnas)
fig = px.scatter(df,x='Celdas', y="Presion", animation_frame="Tiempo",color='Celdas',
	size='Tiempo',size_max=30,range_y=[0,5300])
fig.show()
plt.show()