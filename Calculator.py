def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero is not allowed."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide)
    }

    print("Simple Calculator")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    while True:
        choice = input("Select operation (1/2/3/4): ")

        if choice in operations:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            print(f"{num1} {operation_name} {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

        if input("Do you want to perform another calculation? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
