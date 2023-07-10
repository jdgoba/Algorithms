vector=[7,4,5,9,4]

N=len(vector)

for i in range(0,N):
	for j in range(0,N-1-i):
		if vector[j+1]<vector[j]:
			aux=vector[j+1]
			vector[j+1]=vector[j]
			vector[j]=aux

print(vector)



