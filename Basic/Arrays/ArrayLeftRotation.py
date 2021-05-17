def rotLeft(a, d):
    i = 0
    tempArray = []               #using a temporary array to store the initial elements required to rotate
    while (i < d):               #storing the elements in temporary array
        tempArray.append(a[i])   
        i = i + 1
    i = 0
    while (d < len(a)):          #moving the remaining to the start of array
        a[i] = a[d]
        d +=1
        i +=1
    a[0:] = a[0: i] + tempArray  #concatenate two arrays
    return a


arr=[1,2,3,4,5,6]
print(rotLeft(arr,3))