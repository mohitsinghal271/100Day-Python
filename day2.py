print("welcome to the tipe calculateor")
total_bill=input("Whata was the total bill?")
tip= float(input("How much tip you want to give 10,12,15 percent?"))
num_people=input("How many people to split the bill?")

print(float(total_bill*(1+(tip/100))/num_people))
