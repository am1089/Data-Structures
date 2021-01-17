import random
import time

def sort():
    starttime = time.time()
    size = int(input('How big is the list: '))
    RANGE = int(input('What will be the max value: '))
    numbers = []
    for i in range(0, size):
        n = random.randint(1, RANGE)
        numbers.append(n)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
             numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)
    print(time.time() - starttime)

sort()