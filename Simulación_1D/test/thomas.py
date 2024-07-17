def thomas(C0,C2,C5,b):
	n=len(C0)
	P=[0]*n
	x=C0
	for i in range(n-1):
		a=C2[i]/x[i]
		x[i+1]=x[i+1]-a*C5[i]
		b[i+1]=b[i+1]-a*b[i]
	P[n-1]=b[n-1]/x[n-1]
	for i in range(n-2,-1,-1):
		P[i]=(b[i]-C5[i]*P[i+1])/x[i]
	return P