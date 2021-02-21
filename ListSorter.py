import random
from random import randint
import time

def bubblesort(array, switch):
    p = len(array)
    k = 1
    for i in range(p - k):
        for j in range(i + 1, p):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                k += 1
        if switch == array:
            break
        else:
            switch = array.copy()
            continue   
    return
def quicksort(array):
    if len(array) <= 1:
        return array

    left  = []
    right = []
    equal = []
    pivot = array[0]
    for num in array:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    leftside = quicksort(left)
    rightside = quicksort(right)
    finallist = leftside + equal + rightside 
    return finallist

size = int(input('How big is the list: '))
RANGE = int(input('What will be the max value: '))
numbers = []
switch = []
for i in range(0, size):
    n = random.randint(1, RANGE)
    numbers.append(n)
    switch.append(n)

def testAscending(nums):
    status = False
    if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
        status = True
    return status

starttime = time.time()  
# bubblesort(numbers, switch)
NewList = quicksort(numbers)
endtime = time.time() - starttime
print("List sorted: " + str(testAscending(NewList)))
print(endtime)

