import random
import sys

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?$%&"

password_len = int(input("What length would you like your password to be: "))
password_count = int(input("How many passwords would you like: "))
with open("logs.txt", "a") as file:
    for i in range(password_count):
        password = ""
        for j in range(password_len):
            password_char = random.choice(chars)
            password = password + password_char
        file.write("Here's your password: " + password + "\n")
print(f"{password_count} passwords have been saved to logs.txt.")
sys.exit()
