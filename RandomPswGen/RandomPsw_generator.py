# Random Password Generator

import random
import string

l = int(input("Enter the lenghth of your password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(l):
    password += random.choice(characters)

print("The generated password is:" , password)