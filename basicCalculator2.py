# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

# Function to perform floor division
def floorDivide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x // y

# Function to perform modulus operation
def modulus(x,y):
    return(x%y)

# Function to get power
def power(x,y):
    return x**y

while True:
    # Get user input for two numbers and the operation
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Choose an operation (+, -, *, /,//,%,^): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    # Perform the selected operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation == '//':
        result = floorDivide(num1, num2)    
    elif operation == '%':
        result = modulus(num1,num2)
    elif operation == "^":
        result = power(num1,num2)
    else:
        print("Invalid operation. Please choose +, -, *, /, //, % , or ^.")
        continue

    # Display the result
    print(f"Result: {result}")

    # Ask if the user wants to perform another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != "yes":
        break
