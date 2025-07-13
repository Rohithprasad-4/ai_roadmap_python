#GRADEcalculator
a = int(input("enter the numbers:"))
def grade(a):
    if (a >= 90):
        print("You got grade 'O'")
    elif (a >= 80):
        print("You got grade 'A+'")
    elif (a >= 70):
        print("You got grade 'A'")
    elif (a >= 60):
        print("You got grade 'B+'")
    elif (a >= 50):
        print("You got grade 'B'")
    elif (a >= 40):
        print("You got grade 'C'")
    elif (a >= 30):
        print("You got grade 'F'")
    else:
        print("Please eneter vaild marks")

print(grade(a))