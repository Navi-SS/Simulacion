import numpy as np

dt = 60
tf = 360
cima = np.array([0,9400, 9350, 9300, 9360, 9420,0])
p_ref = 6500
d_ref = 9442.5
densidad = 60.476
dx = np.array([0,1000,1000,1000,1000,1000,0]) #ft
dy = np.array([0,900,900,900,900,900,0]) #ft
dz = np.array([0,85,85,85,85,85,0]) #ft
n = len(dx)
vis = 3 #cp
kx = np.array([0,8,8,8,8,8,0]) #mD
bo = 1.05 #rbl/stb
co = 3.5E-6 #psi^-1
poro = np.array([0,0.22,0.22,0.22,0.22,0.22,0]) #fracción
q = np.array([0,0,0,-125,0]) #BPD
b = 1.03
ac = 5.615
bc = 0.001127
gp = 0