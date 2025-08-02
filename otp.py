import random
a=random.randint(1000000,9999999)
print(a)
p=int(input("enter otp"))
if(p==a):
    print("otp is corrrect")
else:
    print("otp is wrong")
