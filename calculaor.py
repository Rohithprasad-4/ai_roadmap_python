#calculaor
A = float(input("enter a first number "))
B = float(input("enter a second number "))
C = input("enter a operation")
def calculator(A,B,C):
    if (C == '+'):
        print("sum is", A+B)
    elif (C == "-"):
        print("subraction is",A-B)
    elif (C == "*"):
        print("multipilcation is",A*B)
    elif (C == "/"):
        print("divion is",A/B)
    elif (C == "%"):
        print("modulus is",A%B)
    else:
        print("Invaid operator")
print("Result",calculator(A,B,C))
    

        