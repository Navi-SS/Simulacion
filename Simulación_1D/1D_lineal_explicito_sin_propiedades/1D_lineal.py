import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

P0=[0,4000,4000,4000,4000,0]
dx=200
dt=10
tf=360
tiempo=[0]

columnas=['Celda1','Celda2','Celda3','Celda4']
presiones=pd.DataFrame(columns=columnas)
presiones.loc[0]=P0[1:-1]

P1=P0
for t in range(dt,tf+1,dt):
	tiempo.append(t)
	for i in range(1,len(P0)-1):
		P1[i]=(P0[i-1]-2*P0[i]+P0[i+1])/dx**2*dt+P0[i]
	P0=P1
	presiones.loc[t/dt]=P0[1:-1]

var1=sorted(columnas*len(tiempo))
df=pd.DataFrame(columns=['Presion','Celdas','Tiempo'])
df['Presion']=presiones.to_numpy().flatten(order='F')
df['Celdas']=sorted(columnas*len(tiempo))
df['Tiempo']=tiempo*len(columnas)

fig = px.line(df, x="Tiempo", y="Presion", color='Celdas')
fig.show()
plt.show()

fig = px.scatter(df, x='Celdas', y="Presion", animation_frame="Tiempo",color='Celdas',
	size='Tiempo',size_max=30,range_y=[3900,4000])
fig.show()
plt.show()
