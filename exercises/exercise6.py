# Python Calculator

operator = input("Enter the operator (+ - / *): ")
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))

if operator == "+":
    result = round(a + b)
    print(result)
elif operator == "-":
    result = round(a - b)
    print(result)
elif operator == "*":
    result = round(a * b)
    print(result)
elif operator == "/":
    result = round(a / b)  
    print(result)
else:
    print(f"The operator is not valid.")