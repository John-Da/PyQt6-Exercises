def calculate_and_convert(num1, num2):
    try:
        if num1 is ValueError:
            if num2 is ValueError:
                raise ValueError
        else:
            answer = (float(num1) + float(num2)) * 2
            return int(answer)
    except ValueError:
        return "Error: Invalid input. Please enter numbers only."


print(calculate_and_convert(3, 2))
print(calculate_and_convert(3, 2.5))
print(calculate_and_convert(3.14, 2.5))
print(calculate_and_convert("a", 5))
print(calculate_and_convert(6, "b"))
