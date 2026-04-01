'''def greet_with(name,location):
        print(f"Hello {name}")
        print(f"what is it like in {location}")

greet_with("Mohit","vidisha")

'''

def calculate_love_score(name1,name2):
    name=(name1+name2).lower()

def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    true_letters = "true"
    love_letters = "love"
    
    true_score = 0
    love_score = 0
    
    for char in combined:
        if char in true_letters:
            true_score += 1
        if char in love_letters:
            love_score += 1
    
    print(int(str(true_score) + str(love_score)))
    
    
    
    
    
    
    
     
    
calculate_love_score("Kanye West", "Kim Kardashian")