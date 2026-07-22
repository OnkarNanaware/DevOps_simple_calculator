a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

def addition(a,b):
	result = a + b
	print("Addition: " + (result))

def subtraction(a,b):
    result = a + b
    print("Subtraction: " + (result))
    
def multiplication(a,b):
    result = a * b
    print("Multiplication: " + (result))
    
def divison(a,b):
    result = a / b
    print("Division: " + (result))
    
def modulus(a,b):
    result = a % b
    print("Modulus: " + (result))
    
addition(a,b)
subtraction(a,b)
multiplication(a,b)
division(a,b)
modulus(a,b)