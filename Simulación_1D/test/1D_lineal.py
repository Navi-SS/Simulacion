# Import packages
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

from datos import *

columas = ['Celda1','Celda2','Celda3','Celda4','Celda5']
presiones = pd.DataFrame(columns=columas)
presiones.loc[0] = P0[1:-1]

ax, vb = [], []
# Calculate Area & Volume
for i in range(N):
    ax.append(DZ[i]*DY[i])
    vb.append(DX[i]*DZ[i]*DY[i])

# Generate A matrix
c2,c5,gt,tiempo = np.array([]), np.array([]), np.array([]), [0]
for i in range(1, N-1):
    try:
        c2 = np.append(c2, (2 * ax[i]* KX[i] * ax[i-1] * KX[i-1]) / (ax[i] * KX[i] * DX[i-1] + ax[i-1] * KX[i-1] * DX[i]) * (BC / (BO * VIS)))
        c5 = np.append(c5, (2 * ax[i] * KX[i] * ax[i+1] * KX[i+1]) / (ax[i] * KX[i] * DX[i+1] + ax[i+1] * KX[i+1] * DX[i]) * (BC / (BO * VIS)))
        gt = np.append(gt, (AC * B * DT) / (vb[i] * PORO[i] * CO))
    except:
        pass
# Change NaN to Zero
c2=np.nan_to_num(c2)
c5=np.nan_to_num(c5)

P1 = P0
for t in range(DT, TF+1, DT):
    tiempo.append(t)
    for i in range(1, N-1):
        P1[i] = P0[i] + gt[i-1] * (Q[i] + c5[i-1] * (P0[i+1] - P0[i]) - c2[i-1] * (P0[i] - P0[i-1]))
    P0 = P1
    presiones.loc[t/DT] = P0[1:-1]

# Generate animate graph
var1 = sorted(columas*len(tiempo))
df = pd.DataFrame(columns=['Presion', 'Celdas', 'Tiempo'])
df['Presion'] = presiones.to_numpy().flatten(order='F')
df['Celdas'] = sorted(columas*len(tiempo))
df['Tiempo'] = tiempo * len(columas)
fig = px.scatter(df, x='Celdas', y='Presion', animation_frame='Tiempo', color='Celdas',
    size='Tiempo', size_max=30, range_y=[0, 5300])
fig.show()
plt.show()