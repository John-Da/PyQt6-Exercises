def print_info(*data, **info):
    print("Positional arguments:")
    for dataOne in data:
        print(f"- {dataOne}")
    print()
    print("Keyword arguments:")
    for itemOne, itemTwo in info.items():
        print(f"- {itemOne}: {itemTwo}")
        


print_info("Alice", 25, city="New York", job="Developer")
