from functools import partial


def multiply_and_add(x, y, z):
    return x * y + z


double_and_add_five = partial(multiply_and_add, y=2, z=5)
triple_and_add_ten = partial(multiply_and_add, y=3, z=10)


print("double_and_add_five(3):", double_and_add_five(3))
print("double_and_add_five(4):", double_and_add_five(4))

print("triple_and_add_ten(3):", triple_and_add_ten(3))
print("triple_and_add_ten(4):", triple_and_add_ten(4))
