def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiplication(a, b):
    return a * b 

def divide(a, b):
    return a / b 


while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exit done")
        break

    elif choice == 1:
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        print(add(a, b))

    elif choice == 2:
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        print(subtract(a, b))

    elif choice == 3:
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        print(multiplication(a, b))

    elif choice == 4:
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))

        if b != 0:
            print(divide(a, b))
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice, please enter between 1 and 5")