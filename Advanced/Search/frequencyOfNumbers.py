def CountFrequency(lis): 
    dic = {}                      #declaring a dictionary
    resultList=[]                 #creating a  list to store result in desired form

    for i in lis:                  #looping through input list
        if i in dic:               #check if item already exist in dic then add 1 in its value
            dic[i] += 1
        else:                      #else add new item in dic with value 1
            dic[i] = 1

    for i in dic:                  #store result in a list to get results in desired form
        resultList.append({i:dic[i]})
    
    return resultList


array= [1,2,3,4,5,4,3,1]
print(CountFrequency(array))

