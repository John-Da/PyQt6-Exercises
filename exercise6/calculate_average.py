def calculate_average(*numbers, round_to=2):
    try:
        avg = sum(numbers) / len(numbers)
        answer = round(avg, round_to)
        return answer
    except ZeroDivisionError:
        return 0


print(calculate_average(100, 120, 130))
print(calculate_average(10.5, 20.5, 30.5, round_to=1))
print(calculate_average())
