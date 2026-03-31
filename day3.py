'''
bill=0
print("wellcome to python pizza deliveries!")
size = input("what size pizza do you want? S,M OR L:")
if size =="S":
    bill=15
   
elif size =="M":
    bill =20
  
else size =="l":
    bill =25
    
    pepperoni=input("do you want pepperoni on your pizza ? Y or N:")
    if pepperoni =="Y":
        bill +=2
    extra_cheese=input("do you want extra cheese? Y or N:")
    if extra_cheese =="Y":
        bill +=1
    print(f"your final bill is {bill}")
    
'''

print("wellcome to the treasure island")
print("your mission is to find the treasure")

choice=input("left or right")
if choice =="left":
    choice=input("swim  or wait")
    if choice =="wait":
        choise = input("Which door red or blue")
        if choise =="blue":
            print("you win")
        else:
            print("you losse")
    else:
        print("you losse")
else:
    print("you losse")