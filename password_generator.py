import random
import string

print("---- Password Generator ----")

length = int(input("Enter password length: "))

use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = string.ascii_letters

if use_numbers == "y":
    characters += string.digits

if use_symbols == "y":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)