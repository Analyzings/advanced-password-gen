import random
import os
import sys

strong_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};':\"<>,.?/\\|"
medium_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
weak_chars = "abcdefghijklmnopqrstuvwxyz1234567890"

def get_password_length():
    password_len = int(input("what length would you like your password to be: "))
    while password_len < 8:
        print("password length must be at least 8 characters.")
        password_len = int(input("what length would you like your password to be: "))
    return password_len

def get_password_count():
    password_count = int(input("how many passwords would you like: "))
    while password_count <= 0:
        print("number of passwords must be greater than 0.")
        password_count = int(input("how many passwords would you like: "))
    return password_count

def get_password_strength():
    strength = input("Choose password strength (strong/medium/weak): ").lower()
    while strength not in ["strong", "medium", "weak"]:
        print("Invalid password strength. Choose either strong, medium or weak.")
        strength = input("Choose password strength (strong/medium/weak): ").lower()
    return strength

password_len = get_password_length()
password_count = get_password_count()
password_strength = get_password_strength()

if password_strength == "strong":
    chars = strong_chars
elif password_strength == "medium":
    chars = medium_chars
else:
    chars = weak_chars

# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

i = 1
while True:
    log_file = os.path.join(script_dir, f"logs{i}.txt")
    if not os.path.exists(log_file):
        break
    i += 1

with open(log_file, "w") as file:
    for j in range(password_count):
        password = ""
        for k in range(password_len):
            password_char = random.choice(chars)
            password = password + password_char
        file.write("here's your password with strength '{}': {}\n".format(password_strength, password))

print(f"{password_count} passwords with strength '{password_strength}' have been saved to {log_file}.")
sys.exit()
