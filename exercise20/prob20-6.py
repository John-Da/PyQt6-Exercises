

class StringManipulator:
    def manipulate(self, text):
        return text.lower()
    

class AdvancedStringManipulator(StringManipulator):
    def manipulate(self, text, custom):
        return custom(super().manipulate(text))
    


basis_manipulator = StringManipulator()
advanced_manipulator = AdvancedStringManipulator()

custom_manipulation = lambda x: x[::-1].upper()
# test_string = "Hello, World!"
# print(custom_manipulation(test_string))


test_string = "Hello, World!"
print("Original string:", test_string)
print("Basic manipulation:", basis_manipulator.manipulate(test_string))
print("Advanced manipulation:", advanced_manipulator.manipulate(test_string, custom_manipulation))

eval_expression = ("advanced_manipulator.manipulate('Python is Fun!', custom_manipulation)")

eval_result = eval(eval_expression)
print(f"Eval result of '{eval_expression}':", eval_result)
print("Advanced manipulation (capitalize):", advanced_manipulator.manipulate(test_string, str.capitalize))

print("Advanced manipulation (remove vowels):", advanced_manipulator.manipulate(test_string, lambda s: ''.join(c.lower() for c in s if c not in 'aeiou')))


