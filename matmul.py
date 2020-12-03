def multiply(m1,m2):
	l =list()
	m3 =list()
	for i in range(len(m1)):
		l=list()
		for j in range(len(m2[0])):
			temp =0
			for k in range(len(m2)):
				temp += m1[i][k] *m2[k][j]
			l.append(temp)
		m3.append(l)
	return m3

def tranpose(m):
	m2 = list()
	for i in range(len(m[0])):
		l = list()
		for j in range(len(m)):
			l.append(m[j][i])
		m2.append(l)
	return m2

def scale(m,n):
	m2 = list()
	for i in range(len(m[0])):
		l = list()
		for j in range(len(m)):
			l.append(m[i][j]*n)
		m2.append(l)
	return m2




