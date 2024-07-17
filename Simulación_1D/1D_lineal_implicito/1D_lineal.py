from datos import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from thomas import *

columnas=['Celda1','Celda2','Celda3','Celda4','Celda5']
presiones=pd.DataFrame(columns=columnas)
presiones.loc[0]=P0

#Se calcula área y volumen
Ax=[dz[i]*dy[i] for i in range(n)]
Vb=[dx[i]*dz[i]*dy[i] for i in range(n)]
c2,c5,gt,tiempo=np.array([]),np.array([]),np.array([]),[0]
for i in range(1,n-1):
	try:
		c2=np.append(c2,(2*Ax[i]*kx[i]*Ax[i-1]*kx[i-1])/(Ax[i]*kx[i]*dx[i-1]+Ax[i-1]*kx[i-1]*dx[i])*(Bc/(Bo*vis)))
		c5=np.append(c5,(2*Ax[i]*kx[i]*Ax[i+1]*kx[i+1])/(Ax[i]*kx[i]*dx[i+1]+Ax[i+1]*kx[i+1]*dx[i])*(Bc/(Bo*vis)))
		gt=np.append(gt,(Vb[i]*poro[i]*Co)/(Ac*B*dt))
	except:
		pass
c2=np.nan_to_num(c2)
c5=np.nan_to_num(c5)
c0=[-1*(c2[i]+c5[i]+gt[i]) for i in range(n-2)]
C0=tuple(c0)
b=[0]*(n-2)
for t in range(dt,tf+1,dt):
	tiempo.append(t)
	for i in range(n-2):
		b[i]=-q[i]-gt[i]*P0[i]
	P0=thomas(c0,c2[1:],c5[:-1],b)
	c0=list(C0)
	presiones.loc[t/dt]=P0

#Graficar

var1=sorted(columnas*len(tiempo))
df=pd.DataFrame(columns=['Presion','Celdas','Tiempo'])
df['Presion']=presiones.to_numpy().flatten(order='F')
df['Celdas']=sorted(columnas*len(tiempo))
df['Tiempo']=tiempo*len(columnas)

fig = px.line(df, x="Tiempo", y="Presion", color='Celdas')
fig.show()
plt.show()

fig = px.scatter(df,x='Celdas', y="Presion", animation_frame="Tiempo",color='Celdas',
	size='Tiempo',size_max=30,range_y=[0,5300])
fig.show()
plt.show()