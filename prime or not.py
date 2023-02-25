num=int(input("Enter a number greater than 1\t"))
flag=0
for i in range(2,num):
    if num%i == 0:
        flag=1
        break
if flag==0:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is NOT a Prime Number")
