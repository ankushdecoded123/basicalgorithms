# bubblesort() method
def bubbleSort(arr, size):
    if size > 2:

        for i in range(size-1):
            if arr[i] > arr[i+1]:
                #swap values (arr[i], arr[i+1])
                arr[i], arr[i+1] = arr[i+1], arr[i]

        #recusive call -> bubbleSort()
        bubbleSort(arr, size-1)
            

# method to print an array
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ") 
    print("\n")
        
# driver method
if __name__ == '__main__': 
    arr = [3,4,1,7,6,2,8]  
    size=len(arr)
    print ("Given array: ", end="\n")  
    printList(arr)
    bubbleSort(arr, size) 
    print("Sorted array: ", end="\n") 
    printList(arr)
