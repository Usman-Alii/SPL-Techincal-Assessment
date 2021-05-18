#In memoization solution of fibonacci the calculated results are stored in an array and recursive call look up already calculated results in the array 
#instead of calculating them again and use them. In this way the programme becomes faster

fibonacci_cache = {}                       #list to store calculated results
def fibonacci_memo(input_value):
    if input_value in fibonacci_cache:                     #check if the result exist in list
        return fibonacci_cache[input_value]                #return already calculated result
    if input_value == 0:                                   #check if input value is 0 ,1 or 2
            value = 0
    elif input_value == 1:
            value = 1
    elif input_value == 2:
            value = 1
    elif input_value > 2:                                  #check if input is grater than 2     
            value =  fibonacci_memo(input_value -1) + fibonacci_memo(input_value -2)         #recursive call
    fibonacci_cache[input_value] = value                   #store calculated result in array
    return value

print(fibonacci_memo(5))