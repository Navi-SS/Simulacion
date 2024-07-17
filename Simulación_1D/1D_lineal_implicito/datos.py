import numpy as np
dt=20
tf=360
dx=np.array([0,1500,1200,1320,1480,1500,0]) #ft
dy=np.array([0,800,870,700,1000,800,0]) #ft
dz=np.array([0,70,75,80,69,70,0]) #ft
n=len(dx)
vis=9 #cp
kx=np.array([0,60,65,53,84,60,0]) #mD
Bo=1.01 #rbl/stb
Co=3.5E-6 #psi^-1
poro=np.array([0,0.27,0.21,0.16,0.19,0.27,0]) #fracción
P0=np.array([5300,5300,5300,5300,5300]) #psia
q=np.array([0,-260,0,-130,0]) #BPD
B=1.01
Ac=5.615
Bc=0.001127