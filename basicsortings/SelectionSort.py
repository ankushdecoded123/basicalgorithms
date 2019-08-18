# selectionsort() method
def selectionSort(arr):
	arraySize = len(arr)

	for i in range(arraySize):
		min = i

		for j in range(i+1, arraySize):

			if arr[j] < arr[min]:
				min = j
                
			#swap values
		arr[i], arr[min] = arr[min], arr[i]


# method to print an array
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ") 
    print("\n")
        
# driver method
if __name__ == '__main__': 
    arr = [3,4,1,7,6,2,8]  
    print ("Given array: ", end="\n")  
    printList(arr)
    selectionSort(arr) 
    print("Sorted array: ", end="\n") 
    printList(arr)