import math

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

def addition(a, b):
    print("Addition:", a + b)

def subtraction(a, b):
    print("Subtraction:", a - b)

def multiplication(a, b):
    print("Multiplication:", a * b)

def division(a, b):
    if b != 0:
        print("Division:", a / b)
    else:
        print("Error: Cannot divide by zero")

def modulus(a, b):
    print("Modulus:", a % b)

def power(a, b):
    print("Power:", a ** b)

def average(a, b):
    print("Average:", (a + b) / 2)

def square_root(a):
    print("Square root of first number:", math.sqrt(a))


print("\n--- Calculator Results ---")

addition(a, b)
subtraction(a, b)
multiplication(a, b)
division(a, b)
modulus(a, b)
power(a, b)
average(a, b)
square_root(a)
