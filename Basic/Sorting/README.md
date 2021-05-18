# Sorting Problems:

## Problem 1: Distribute An Array of Numbers around a given pivot

    Given an Array of integers and pivot integer return an array
    that ditributes the array around that pivot in a sorted order.

    Example:

        For An Array
        [1,-1,-2,2,-3,3,0] the sorted array would be
        [-3,-2,-1,0,1,2,3] for pivot 0;

        Function Description

        Complete the function DistributeArray with following details:

        DistributeArray has the following parameter(s):
            int[n] a: Array of integers
            int b: pivot

        Returns
            int[n] a'

        Questions:
            How do we find the pivot in the array containing even number of elements?
            Ans:we can find the pivot of an array containing even number of elements by taking an average of middle two elements.
            
            (Array[(size of array/2)]+Array[(size of array/2+1)])/2


    Command/Script to Run Problem 1: python DistributeNumbersAroundPivot.py 

## Problem 2: Find maximum number from a list of numbers (both negative and non-negative).

    Given an array of positive and negative integers write a
    sorting algorithm to return the maximum value.

    Note: Smart Choice of sorting algorithm is important.

    Example:

        int[] arr  = [-1,1,-2,2,-3,3,0] returns 3;

        int[] arr'  = [1,2,3,4,5,0] returns 5;

    Questions:

       Can we use the method DistributiveArray written above to achieve this?
       Ans:we can use the DistributiveArray function to sort the array and then we can find maximum at the end of array.


    Command/Script to Run Problem 2: python findMaxium.py
