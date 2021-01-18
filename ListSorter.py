import random
import time

size = int(input('How big is the list: '))
RANGE = int(input('What will be the max value: '))
numbers = []
switch = []
for i in range(0, size):
    n = random.randint(1, RANGE)
    numbers.append(n)
    switch.append(n)

def sort(numbers, switch):
    p = len(numbers)
    starttime = time.time()
    k = 1
    for i in range(p - k):
        for j in range(i + 1, p):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                k += 1
        if switch == numbers:
            break
        else:
            switch = numbers.copy()
            continue    
    print(numbers)
    print(time.time() - starttime)

sort(numbers, switch)