lista=[7,4,5,9,4]

def cocktail_sort(array):
	length=len(array)
	left=0
	right=length-1

	while left<right:

		i=left
		j=right

		while i<right:
			if array[i+1]<array[i]:
				array[i+1],array[i]=array[i],array[i+1]
			i=i+1

		right=right-1

		while j>left:
			if array[j]<array[j-1]:
				array[j],array[j-1]=array[j-1],array[j]
			j=j-1

		left=left+1

	return array

cocktail_sort(lista)
print(lista)
