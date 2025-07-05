# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

while True:
    print("\nSimple Calculator")
    print("Select operation:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting Calculator.")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        except ValueError as ve:
            print("Error:", ve)
    else:
        print("Invalid input. Please choose 1-5.")
