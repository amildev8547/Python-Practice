n=int(input('Enter a number up to which you want to find the average '))
sum=0
for num in range(1,n+1,1):
    sum=sum+num
    average=sum/n
print("The average of",n,"natural numbers is",average)
