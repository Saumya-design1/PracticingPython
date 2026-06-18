import random

def guess_the_number():
    n = random.randint(1,100)
    print("Welcome to Guess the Number!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    guess = 1
    a = 0
    while a != n:
        a = int(input("Enter your guess: "))
        if a < n:
            print("Too low! Try again.")
            guess += 1
        elif a > n:
            print("Too high! Try again.")
            guess += 1
        else:
            print(f"Congratulations! You've guessed the number {n} in {guess} attempts!")

guess_the_number()