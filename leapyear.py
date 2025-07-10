a = int(input("enter a year: "))
if a % 4 == 0 :
    if a % 100 == 0 :
        if a % 400 == 0 :
            print("Its a leap year")
        else:
            print("Its a not leap year")
    else:
        print("Its not a leap year")
else:
    print("Its a leap year")