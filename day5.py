'''fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit +"pie")
    

student_scores=[100,90,80,70,60,43]
sum = 0
for score in student_scores:
    sum += score
print(sum)
  

sum=0
for number in range(1,100):
    sum += number
print(sum)

'''

letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers =['1','2','3','4','5','6','7','8','9','0']
symbols =['@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','/']

print("Welcome to the password generator!")
num_letters = int(input("How many letters would you like in your password?"))
num_numbers = int(input("How many numbers would you like in your password?"))
num_symbols = int(input("How many symbols would you like in your password?"))

password = []
for letter in range(num_letters):
    password.append(random.choice(letters))
for number in range(num_numbers):
    password.append(random.choice(numbers))
for symbol in range(num_symbols):
    password.append(random.choice(symbols))


print(random.shuffle(password))
