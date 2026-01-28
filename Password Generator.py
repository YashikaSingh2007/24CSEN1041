import random
import string

length = int(input("Enter password length: "))
characters= string.ascii_letters + string. digits + string.punctuation
password= ""

for i in range(length):
    password += random.choice(characters)

print("The generated password is:", password)


# OUTPUT:
Enter password length: 12
The generated password is: bZw/`]%F~hv/

Enter password length: 5
The generated password is: r(%c_

Enter password length: 26
The generated password is: {YO#d)]KZ,(=MW}+x_s%4+!w(s





