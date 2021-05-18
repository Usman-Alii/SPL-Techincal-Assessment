
def minAbsDiff(lis):

    n=len(lis)
    if n <=1:       
        return
    minAbsDiff = abs(lis[1] - lis[0])          #check the abs difference of first 2 elements and store it 
     
    for i in range(2, n):                   #check abs difference of all other elements adjacent to each other in list
        minAbsDiff = min(minAbsDiff, abs(lis[i] - lis[i - 1]))  
    res = min(minAbsDiff, abs(lis[n - 1] - lis[0]))    #check the abs iff of last and first element
    return res
 
arr = [10, 12, 13, 15, 10]
print(minAbsDiff(arr))