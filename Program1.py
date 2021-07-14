num = float(input( " a ="))
op = input("Enter the Operator")
num1 = float(input(" b = "))

if op == "Addition":
    print(num + num1)
elif op == "Subraction":
    print(num - num1)
elif op == "Multipliction":
    print(num * num1)
elif op == "Divison":
    print(num / num1)
else:
    print("Invalid Number")