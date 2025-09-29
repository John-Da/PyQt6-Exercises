def execute_list_comprehension(eq):
    try:
        result = eval(eq)
        if isinstance(result, (float, int, str, list, dict, tuple)):
            print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")


execute_list_comprehension("[x**2 for x in range(5)]")
execute_list_comprehension("[name.upper() for name in ['alice', 'bob', 'charlie']]")
execute_list_comprehension("This is not a valid list comprehension")
