import math


def process_numbers(numbers):
    new_numberList = []
    for num in numbers:
        if num > 0:
            num = math.pow(num, 2)
            new_numberList.append(num)

    total_sum = sum(new_numberList)
    total_sum = int(total_sum)
    if total_sum % 2 == 1:
        return f"Odd Sum: {total_sum}"
    else:
        return f"Even Sum: {total_sum}"


print(process_numbers([1, -2, 3, -4, 5]))
print(process_numbers([2, 4, 6, 8]))
print(process_numbers([1.2, 4, -6.3, 8]))
