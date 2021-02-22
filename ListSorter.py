import random
from random import randint
import time
import matplotlib.pyplot as plt

def bubblesort(array):
    swap = False
    p = len(array)
    k = 1
    for i in range(p - k):
        for j in range(i + 1, p):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swap = True
                k += 1
        if swap == False:
            break
    return array

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

def testAscending(nums):
    status = False
    if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
        status = True
    return status

x1 = []
y1 = []
x2 = []
y2 = []

for index in range(1, 6):
    size = 10**index
    maxval = 10**9
    numbers = []
    for i in range(0, size):
        n = random.randint(1, maxval)
        numbers.append(n)
        
    starttime = time.time()  
    NewList = quicksort(numbers)
    endtime = time.time() - starttime
    print("QSort List sorted: " + str(testAscending(NewList)))
    print(endtime)
    x1.append(size)
    y1.append(endtime)

    starttime = time.time()
    NewList = bubblesort(numbers)
    endtime = time.time() - starttime
    print("BSort List sorted: " + str(testAscending(NewList)))
    print(endtime)
    x2.append(size)
    y2.append(endtime)

# plotting the line 1 points
plt.plot(x1, y1, label = "Quick Sort")
# plotting the line 2 points
plt.plot(x2, y2, label = "Bubble Sort")

# naming the x axis
plt.xlabel('Array Size')
# naming the y axis
plt.ylabel('Sort Time')
# giving a title to my graph
plt.title('Compare Sort Time')
# show a legend on the plot
plt.legend()
  
# set graph scale
plt.xscale('log')
plt.yscale('log')

# function to show the plot
plt.show()