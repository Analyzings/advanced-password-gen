
import random
import sys

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?$%&"

while 1:
    password_len = int(input("What lenght would you like your pass to be : "))
    password_count = int(input("How many passwords would you like (max is 1 for now): "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
            with open('log.txt', 'w') as sys.stdout:
                print("Here's your pass : ", password)

  