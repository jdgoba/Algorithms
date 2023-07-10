lista=[7,4,5,9,4]

def insertion_sort(array):
	for i in range(1,len(array)):
		index=array[i]

		j=i-1

		while j>=0 and index<array[j]:
			array[j+1]=array[j]
			j=j-1
		array[j+1]=index

	return array

insertion_sort(lista)
print(lista)

