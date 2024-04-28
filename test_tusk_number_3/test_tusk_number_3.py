def dyapozon():
    start = int(input('введите первое число: '))
    end = int(input('введите последнее число: '))

    list_numbers = []
    numbers = range(start, end + 1)

    for number in numbers:
        list_numbers.append(number)
    print(list_numbers)

dyapozon()