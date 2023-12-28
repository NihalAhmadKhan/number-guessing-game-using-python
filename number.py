import random as r
cn=r.randrange(1,101)
user=int(input("Enter Your Number : "))
print("Computer number :",cn)
if user>cn:
  print("Your guess number is high")
elif user<cn:
  print("Computer guess number is high")
else:
  print("Your numbers are equal")
