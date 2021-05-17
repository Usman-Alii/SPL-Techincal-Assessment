def SharedSubString(str1,str2):
    dic={}                             #declare an empty dictionary
    for i in str1:                     #push all the elements of first string in dictionary as key with value 1
        dic.update({i:"1"})
    for i in str2:                      #check if any sub string of string 2 exist in dictionary of string 1
        if(i in dic):
            return 1

    return 0

print(SharedSubString("abc","hgs"))