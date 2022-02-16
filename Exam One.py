count = 0

print("Hello! What is your name?") 
name = (input("Enter Name: "))
print("Well " + name + ", I am thinking of a Number between 1 and 20.")
print("You have 5 guesses.")

import random
r1 = random.randint(1, 20)

for i in range(1, 6):

    count = count + 1
    
    guess = int(input("Take a Guess: "))
    if guess > r1: print("Your Guess is too High.")
    if guess < r1: print("Your Guess is too Low.")
    if guess == r1: print("Good Job, " + name + "! " + "You Guessed my Number in " + "{}".format(count) + " Guesses!" ) (quit())
else: print("Nope. The Number I was Thinking of was: " + "{}".format(r1))