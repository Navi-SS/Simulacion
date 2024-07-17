import math

DT = 1
TF = 15
AREA = 43560 # Acre
RE = ((AREA * 43560) / math.pi) ** 0.5
RW = 0.25 # ft
D_TETA = 2 * math.pi
DZ = [0, 30, 30, 30, 30, 30, 0] # Ft
VIS = 0.5 # Cp
KR = 150 # MD
BO = 1 # Rbl/stb
CO = 1E-5 # Psi^-1
PORO = [0, 0.23, 0.23, 0.23, 0.23, 0.23, 0] # Fracción
P0 = [4000, 4000, 4000, 4000, 4000] # Psia
Q = [0, 0, 0, 0, 0] # BPD
B = 1
AC = 5.615
BC = 0.001127
Q_IZQ = -2000 #BPD
Q_DER = 0 # BPD
N = len(P0)