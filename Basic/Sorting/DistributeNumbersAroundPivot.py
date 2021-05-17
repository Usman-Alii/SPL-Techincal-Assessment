# I am using quick sort algorithm to solve this problem 

def partition(arr, low, high, pivot):                   #In addition to partition function I am giving pivot point to the it so i can distibute array around desired pivot point
    i = (low-1)         # index of smaller element       
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[pi] is now
        # at right place
        pi = partition(arr, low, high,arr[high])
  
        
        
        quickSort(arr, low, pi-1)                       #sort elements before
        quickSort(arr, pi+1, high)                      # sort elements after partition


def DistributeArray(arr, pivot):
    n=len(arr)-1                                        #higher index of array
    indexOfPivot=partition(arr,0,n,pivot)               #getting the index of pivot element after distributing array around it
    quickSort(arr,0,indexOfPivot-1)                     #sort the elements before pivot point
    quickSort(arr,indexOfPivot+1,n)                     #sort elements after pivot point
    return arr
    


array=[1,-1,-2,2,-3,3,0]
print(f"input Array:{array}")
print(f"output Array:{DistributeArray(array,0)}")