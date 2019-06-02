"""
Write a password generator in Python. 
Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. 

The passwords should be random, generating a new password 
every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. 
For weak passwords, pick a word or two from a list.
"""
#to do: imoport a wordlist to generate easy passwords from


# generate a password with length "passlen" with no duplicate characters in the password

import random
import string

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print(p)

# Or one with asking how many chars the password should be
def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return "".join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))