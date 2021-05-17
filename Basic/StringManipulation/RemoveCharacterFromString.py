def RemoveCharacter(str,char):
    noOfOccur = str.count(char)            #find number of occurences of given character in string
    str = list(str)                        #convert string into list
    while noOfOccur:                       #remove all the occurences of given character from list
        str.remove(char)
        noOfOccur-=1

    str = '' . join(str)                   #join the list with empty string
    return str

str="assalam o alaikum"
print(f"input string:{str}")
print(f"output string:{RemoveCharacter(str,'a')}")
