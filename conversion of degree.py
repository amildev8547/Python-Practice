choice=input("To convert Celsius to Fahrenheit,Press (C) \nTo convert Fahrenheit to Celsius,Press (F) \n Enter your choice: ")
if choice=='c' or choice=='C':
    celsius=float(input("Enter your degree in Celsius"))
    fahr=(celsius*(9/5) + 32)
    print(f"{celsius} degree Celsius is {fahr:.2f} degree Fahrenheit ")
elif choice=='f' or choice=='F':
    
        fahr=float(input("Enter your degree in Fahrenheit "))
        celsius=((fahr-32)*(5/9))
        print(f"{fahr} degree Fahrenheit is {celsius:.2f} degree Celsius")
else:
    print("Invalid Input")
