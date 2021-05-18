def DistributiveArray(arr):
	#using selection sort in reverse order	which will find the max in one pass
	i = 0
	MaxNum = arr[0]
	while (i < len(arr)):
		if (MaxNum < arr[i]):
			MaxNum = arr[i]
		i = i + 1
	return MaxNum

arr = [ 1,2,3,-1,-3,-10,10,-99,12,-12 ]
print(DistributiveArray(arr))
