# Simple calculator 
num1 = int(input("Enter value one: "))
num2 = int(input("Enter value two: "))
opr = input("Enter operator (+,-,*,/): ")

if opr == "+":
  print(num1 + num2)
elif opr == "-":
  print(num1 - num2)
elif opr == "*":
  print(num1 * num2)
elif opr == "/":
  print(num1 / num2)
else:
  print("Invalid operator")