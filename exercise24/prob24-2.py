import re


text = input("Enter text:")
pattern = input("Enter pattern:")
found_pattern = re.search(pattern, text)
if found_pattern:
    print(f"Found {pattern} in {text} at {found_pattern.start()}")
else:
    print(f"Cannot find {pattern} in {text}")
