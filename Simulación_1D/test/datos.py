import numpy as np
DT = 1
TF = 360
DX = np.array([0,1500,1200,1320,1480,1500,0]) # Ft
DY = np.array([0,800,870,700,1000,800,0]) # Ft
DZ = np.array([0,70,75,80,69,70,0]) # Ft
N = len(DX)
VIS = 9 # Cp
KX = np.array([0,60,65,53,84,60,0]) # MD
BO = 1.01 # Rbl/stb
CO = 3.5E-6 # Psi^-1
PORO = np.array([0,0.27,0.21,0.16,0.19,0.27,0]) # Fracción
P0 = np.array([0,5300,5300,5300,5300,5300,0]) # Psia
Q = np.array([0,0,-260,0,-130,0,0]) # BPD
B = 1.01
AC = 5.615
BC = 0.001127