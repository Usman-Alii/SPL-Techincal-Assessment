# we can use == operator to compare two dictionaries but here i am going to do a deep comparison of two dictionaries

def compareTwoDic(dic1,dic2):
    keysOfDic1=set(dic1.keys())
    KeysOfDic2=set(dic2.keys())
    if keysOfDic1!=KeysOfDic2:
        return 0

    else:
        for i in dic1:
            if(dic1[i]!=dic2[i]):
                return 0

        return 1


x  = {"a":1,"b":2,"c":3}
b={"c":3,"b":2,"g":3} 
print(compareTwoDic(x,b))
