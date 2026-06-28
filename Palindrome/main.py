print("PALINDROME CHECKER")

text = input("Enter a word: ")
text= text.lower()

reverse_text = text[:: -1]

if text == reverse_text:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
