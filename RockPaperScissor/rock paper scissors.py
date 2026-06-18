
import random


comp = random.choice(['rock', 'paper', 'scissors'])
user = input("Enter your choice (rock, paper, scissors): ").lower()
if user == comp:
    print(f"Both players selected {user}. It's a tie!")

elif user == 'rock':
    if comp == 'scissors':
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")   

elif user == 'paper':
    if comp == 'rock':
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.") 

elif user == 'scissors':
    if comp == 'paper':
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")