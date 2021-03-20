import random

# Input validation
def Input_Valid(input):
    if input != 'NO':
        return True 
    else:
        return False
    
# Order function
def Order(questions, answer, ingredients):   
    print(questions['salty'])
    answer = input('YES/NO:  ')
    if answer == 'YES':
        return ingredients['salty'][random.randrange(0,3,1)]
    if Input_Valid(answer): return "Please type YES or NO"
    print(questions['bitter'])
    answer = input('YES/NO:  ')       
    if answer == 'YES':
        return ingredients['bitter'][random.randrange(0,3,1)]
    if Input_Valid(answer): return "Please type YES or NO"  
    print(questions['sweet'])
    answer = input('YES/NO:  ')
    if answer == 'YES':
        return ingredients['sweet'][random.randrange(0,3,1)]
    if Input_Valid(answer): return "Please type YES or NO"     
    print(questions['fruity'])
    answer = input('YES/NO:  ')
    if answer == 'YES':
        return ingredients['fruity'][random.randrange(0,3,1)]
    if Input_Valid(answer): return "Please type YES or NO"      
    else:
        return "Not available"

# Drive program
if __name__ == '__main__':
    
    questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}
    ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
    print(questions['strong'])
    answer = input('YES/NO:  ')
    if answer == 'YES':
        print(ingredients['strong'][random.randrange(0,3,1)])
    else:
        if answer == 'NO':
            print(Order(questions, answer, ingredients)) 
            print("Thank you !") 
        else:
            print("Order canceled, pLease type YES or NO")
              



