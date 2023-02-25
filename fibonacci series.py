number=int(input("How many terms? "))
f1=0
f2=1
print("Fibonacci Sequence")
print(f1)
print(f2)
i=3
while i<=number:
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
    i+=1
