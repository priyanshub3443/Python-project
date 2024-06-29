from random import randint



random_number=randint(0,10)
print("random_number")


x = -1
while x!= random_number:
  if x!=-1:
    print("worng gusess")
  x= int(input("Enter a number : "))

print("You gusses correctly")

