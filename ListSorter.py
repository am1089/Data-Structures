def sort():
    content = input('Enter in some numbers seperated bt commas: ')
    numbers = content.split(',')
    #print(numbers)
    for num in range(len(numbers)):
        numbers[num] = int(numbers[num])
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
             numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)

sort()