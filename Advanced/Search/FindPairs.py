def findPairs(arr, sum):
 
    lis = []                 #Result List
    alreadyPaired=[]          # List to  store finding pairs
    n=len(arr)
    for i in range(0, n):      #find all the pairs
        for j in range(i + 1, n):
            if arr[i]  and arr[j] not in alreadyPaired:      #If pair already  found then skip this one
                if arr[i] + arr[j] == sum:
                    lis.append((arr[i],arr[j]))               #add pair in  result list
                    alreadyPaired.append(arr[i])              #add pair elements in alreadyPaired list
                    alreadyPaired.append(arr[j])

 
    return lis


arr = [10, 12, 12, 14, 16, 18,12]
print(findPairs(arr,30))