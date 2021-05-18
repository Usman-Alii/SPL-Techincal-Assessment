def calculateMean(lis,size):
    if (size== 1):               #base condition
        return lis[size-1]
    else:
        return ((calculateMean(lis, size - 1) *(size- 1) + lis[size- 1]) / size)          #recursive call
                

arr= [10, 12, 14, 16, 18]
print(calculateMean(arr,len(arr)))