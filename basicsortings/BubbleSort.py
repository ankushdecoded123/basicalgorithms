
# bubblesort() method
def bubbleSort(arr):
	arraySize = len(arr)

	for i in range(arraySize):

		for j in range(0, arraySize-i-1):

			if arr[j] > arr[j+1]:
				#swap values (arr[j], arr[j+1])
				arr[j], arr[j+1] = arr[j+1], arr[j]


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
    bubbleSort(arr) 
    print("Sorted array: ", end="\n") 
    printList(arr)