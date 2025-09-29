

textFile = 'numbers.txt'



first_number = float(input("Enter a number: "))
second_number = float(input("Enter a number: "))


result = f"{first_number} + {second_number} = {first_number + second_number}"
print(result)

with open(textFile ,'w') as numFile:
     # print(result, file=numFile)
     numFile.write(result)
     print('Writing to file numbers.txt')


with open(textFile , 'r' ) as numFile:
     data = numFile.read()
     print('Reading from file numbers.txt')
     print(data)




     