import random

print("Welcome to Password Generator")

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}[];'\":,./<>?\\|"

number = input("Enter number of passwords needed: ")
number = int(number)

length = input("Enter length of password needed: ")
length = int(length)

print("Here are your passwords :)")

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(characters)
    print(password)
