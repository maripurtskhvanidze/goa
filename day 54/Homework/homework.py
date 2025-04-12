try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Please enter valid numbers.")


fruits = ["apple", "banana", "peach"]
try:
    index = int(input("\nEnter an index (0-2): "))
    print("Selected:", fruits[index])
except IndexError:
    print("Index is out of range.")
except ValueError:
    print("Please enter a number.")



info = {"name": "Anna", "age": 16}
key = input("\nEnter a key (name or age): ")
try:
    print("Value:", info[key])
except KeyError:
    print("Key not found.")



s = input("enter a number: ")
try:
    num = int(s)
    print("Converted number:", num)
except ValueError:
    print("Invalid number.")
