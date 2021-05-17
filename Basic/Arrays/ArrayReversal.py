def reverseArray(arr):
    start=0                            #start will be used to iterate array from start
    end=len(arr)-1                 #end will be used to iterate array in reverse order
    while start < end:                 #swap the elements pointed by start and end untill start becomes equal or more than end
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


arr=[1,2,3,4,5]
reverseArray(arr)
print(arr)