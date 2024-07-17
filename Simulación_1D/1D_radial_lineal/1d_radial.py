import math
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

from datos import *
from thomas import thomas

# Datos para el DataFrame
columns = ['Celda1','Celda2','Celda3','Celda4','Celda5']
pressure = pd.DataFrame(columns=columns)
pressure.loc[0] = P0

# Se calcula el espaciamiento algoritmico
alg = (RE / RW) ** (1 / N)

# Se obtienen los radios
r = []
for i in range(1, N+1):
    if i == 1:
        r.append(RW * (alg * math.log(alg)) / (alg - 1))
    else:
        r.append(alg ** (i - 1) * r[0])

# Se calcula el Volumen bruto
vb = []
aux_1 = ((alg ** 2 - 1) ** 2)
aux_2 = (alg ** 2 * math.log(alg ** 2))
for i in range(1, N):
    vb.append(aux_1 / aux_2 * (r[i - 1]) ** 2 * 0.5 * D_TETA * DZ[i])

# Se calcula el ultimo Volumen bruto
aux_3 = alg ** 2 -1
aux_4 = (math.log(alg)/(alg - 1)) ** 2
aux_5 = alg ** 2 * math.log(alg ** 2)
vb.append((1 - (aux_4 * aux_3)/ aux_5) * RE ** 2 * 0.5 * D_TETA * DZ[-2])

# Se obtiene la matriz A
c2, c5, c0, gt= [], [], [], []
for i in range(1, N+1):
    c2.append(BC / (VIS * BO) * (2 * math.pi * KR * DZ[i])/ math.log(alg))
    c5.append(c2[i-1])
    gt.append((vb[i-1] * PORO[i] * CO) / (AC * B * DT))
    c0.append(-(c2[i-1] + c5[i-1] + gt[i-1]))

# Arreglamos unos detalles de la matriz A
c0[0] += c2[0]
c0[-1] += c5[-1]
Q[0] += Q_IZQ
Q[-1] += Q_DER

C0 = tuple(c0)
b = [0] * (N)
time_array = [0]
print(gt)
# Se calcula el tiempo de calculo
for t in range(DT, TF+1, DT):
    time_array.append(t)
    for i in range(N):
        b[i] = -Q[i] - gt[i] * P0[i]
    P0 = thomas(c0, c2[1:], c5[:-1], b)
    c0 = list(C0)
    pressure.loc[t/DT] = P0

# Graficar

var1 = sorted(columns * len(time_array))
df = pd.DataFrame(columns=['Presion','Celdas','Tiempo'])
df['Presion'] = pressure.to_numpy().flatten(order='F')
df['Celdas'] = sorted(columns*len(time_array))
df['Tiempo'] = time_array * len(columns)

fig = px.line(df, x="Tiempo", y="Presion", color='Celdas')
fig.show()
plt.show()

fig = px.scatter(df,x='Celdas', y="Presion", animation_frame="Tiempo",color='Celdas',
	size='Tiempo',size_max=30,range_y=[3500,4050])
fig.show()
plt.show()