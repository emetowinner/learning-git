def fibonacci_genertor(n):
    counter = 0
    first_number, second_number = 0, 1
    if n == 1:
        yield n
    elif n > 1:
        while counter < n:
            yield second_number
            first_number, second_number = second_number, first_number+second_number
            counter += 1
    else:
        print('Out of range')
print(list(fibonacci_genertor(7)))