import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level

password=""

for x in range(0,nr_letters):
    ran_letters = random.choice(letters)
    password += ran_letters

for x in range(0,nr_symbols):
    ran_symbols = random.choice(symbols)
    password += ran_symbols

for x in range(0,nr_numbers):
    ran_numbers = random.choice(numbers)
    password += ran_numbers

print(password)

#hard level


password_list=[]

for x in range(0,nr_letters):
    ran_letters = random.choice(letters)
    password_list += ran_letters

for x in range(0,nr_symbols):
    ran_symbols = random.choice(symbols)
    password_list += ran_symbols

for x in range(0,nr_numbers):
    ran_numbers = random.choice(numbers)
    password_list += ran_numbers

print(password_list)

random.shuffle(password_list)

print(password_list)

password=""
for char in password_list:
    password+=char

print(f"Your password is: {password}")