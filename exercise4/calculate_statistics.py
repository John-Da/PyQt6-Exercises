min_val = 0
max_val = 0
avg_val = 0


def calculate_statistics(number):
    min_val = min(number)
    max_val = max(number)
    count = len(number)
    avg_val = sum(number) / count

    return min_val, max_val, avg_val


data = [4, 2, 7, 1, 9, 5]
min_val, max_val, avg_val = calculate_statistics(data)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val:.2f}")
