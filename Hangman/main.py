import random

list = ["python", "coding", "developer", "computer", "programming"]
word = random.choice(list)

guessed = ["_"]* len(word)
lives = 6

print("Welcome to the hangman game")

while lives > 0 and "_" in guessed:

    print("\n Word:", " ".join(guessed))
    print("Lives left:", lives)

    letter = input("Enter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        
        print("Correct Guess!")
    
    else:
        lives -= 1
        print("Wrong Guess!")
    
if "_" not in guessed:
    print("Congratulations! You won!")
    print("Word was:", word)

else:
    print("Game over!")
    print("Correct Word:", word)
