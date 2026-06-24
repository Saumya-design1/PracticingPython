# QUIZ

ques = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?"
]
options = [
    ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
    ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
    ["A) Au", "B) Ag", "C) Fe", "D) Hg"]
]

answers = ["A", "B", "A"]
score = 0
valid_choices = ["A", "B", "C", "D"]
for i in range(len(ques)):
    print(ques[i])
    for option in options[i]:
        print(option)
    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in valid_choices:
            break
        print("Please enter A, B, C, or D.")
    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", answers[i])
    print()
print("Your final score is:", score)
