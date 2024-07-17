import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from thomas import *
from datos import *

columnas=['Celda1','Celda2','Celda3','Celda4','Celda5']
presiones=pd.DataFrame(columns=columnas)


# Calcular las puntos centrales de celdas y presiones iniciales
d, po = np.array([]), np.array([])
for i in range(1, n-1):
	d = np.append(d,cima[i] + dz[i]/2)
	po = np.append(po, p_ref - (densidad/144) * (d_ref - d[i-1]))

presiones.loc[0]=po
d = np.insert(d, 0, 0)
d = np.insert(d, d.size, 0)

#Se calcula área y volumen
Ax = [dz[i]*dy[i] for i in range(n)]
Vb = [dx[i]*dz[i]*dy[i] for i in range(n)]

# Calcular la matriz tridiagonal
c2, c5, gt, tiempo = np.array([]), np.array([]), np.array([]), [0]
for i in range(1,n-1):
	try:
		c2 = np.append(c2,(2*Ax[i]*kx[i]*Ax[i-1]*kx[i-1])/(Ax[i]*kx[i]*dx[i-1]+Ax[i-1]*kx[i-1]*dx[i])*(bc/(bo*vis)))
		c5 = np.append(c5,(2*Ax[i]*kx[i]*Ax[i+1]*kx[i+1])/(Ax[i]*kx[i]*dx[i+1]+Ax[i+1]*kx[i+1]*dx[i])*(bc/(bo*vis)))
		gt = np.append(gt,(Vb[i]*poro[i]*co)/(ac*b*dt))
	except:
		pass
c2 = np.nan_to_num(c2)
c5 = np.nan_to_num(c5)

# Se calculan las condiciones de frontera

# qscf1 = bc*(kx(1)*Ax(1))/(vis(1)*bo(1))*gp
qscf1 = 50
# qscfn = bc*(kx(n)*Ax(n))/(vis(n)*bo(n))*gp
qscfn=0

# Calculo de efectos potenciales
Qg = np.array([])
for i in range(1,n-1):
	Qg = np.append(Qg, -c5[i-1]*(densidad/144)*(d[i+1]-d[i]) + c2[i-1]*(densidad/144)*(d[i]-d[i-1]))

Qg = np.insert(Qg, 0, -qscf1+c5[0]*(densidad/144)*(d[2]-d[1]))
Qg = np.insert(Qg, Qg.size, -qscfn-c2[-1]*(densidad/144)*(d[-2]-d[-3]))

# Calculamos la diagonal principal
c0 = [-1*(c2[i]+c5[i]+gt[i]) for i in range(n-2)]
C0 = tuple(c0)
b = [0]*(n-2)
for t in range(dt,tf+1,dt):
	tiempo.append(t)
	for i in range(n-2):
		b[i] = -q[i] - gt[i] * po[i] + Qg[i]
	po = thomas(c0, c2[1:], c5[:-1], b)
	c0 = list(C0)
	presiones.loc[t/dt] = po

#Graficar

var1 = sorted(columnas*len(tiempo))
df = pd.DataFrame(columns=['Presion','Celdas','Tiempo'])
df['Presion'] = presiones.to_numpy().flatten(order='F')
df['Celdas'] = sorted(columnas*len(tiempo))
df['Tiempo'] = tiempo*len(columnas)
print (df)
fig = px.line(df, x="Tiempo", y="Presion", color='Celdas')
fig.show()
plt.show()

fig = px.scatter(df,x='Celdas', y="Presion", animation_frame="Tiempo",color='Celdas',
	size='Tiempo',size_max=30,range_y=[5000,7000])
fig.show()
plt.show()