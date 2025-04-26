import random

number = random.randint(1, 10)

for i in range(0, 3):
    gs = int(input('enter your guess'))
    
    if gs == number:
        print("your guess is correct")
        break
    else:
        print("wrong guess, try again")
        
if gs != number:
    print(f"sorry, you've used all of your attempts. the number was {number}")