import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# In order
#
## Prints the password with letters, symbols and numbers in order based on selected amount
#
# password_e= ""
#
# for char in range(1, nr_letters + 1):
#   password_e += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#   password_e += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#   password_e += random.choice(numbers)
#
# print("In order password is:")
# print(password_e)
#


# Random
#
## Prints the password with letters, symbols and numbers in a random order based on selected amount
#
# password_h=[]
#
# for char in range(1, nr_letters+1):
#     password_h.append(random.choice(letters))
#
# for char in range(1, nr_symbols+1):
#     password_h.append(random.choice(symbols))
#
#for char in range(1, nr_numbers+1):
#     password_h.append(random.choice(numbers))
#
# random.shuffle(password_h)
#
# password = ""
# for char in password_h:
#   password += char
#
# print(f"Random password is:")
# print(password)
