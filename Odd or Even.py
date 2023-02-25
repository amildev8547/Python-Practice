#Enter the number to check whether the number is odd or even

num= int(input("Enter the number: "))
mod=num%2
if mod>0:
  print("The number is odd")
else:
  print("The number is even")