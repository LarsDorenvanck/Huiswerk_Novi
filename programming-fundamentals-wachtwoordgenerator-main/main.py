letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '_', '-', '=']



import random

# Vraag de gebruiker om input
nr_letters = int(input("Hoeveel letters wil je in je wachtwoord? "))
nr_symbols = int(input("Hoeveel symbolen wil je in je wachtwoord? "))
nr_numbers = int(input("Hoeveel nummers wil je in je wachtwoord? "))

# Genereer het wachtwoord
password = []

# Voeg letters toe
for _ in range(nr_letters):
    password.append(random.choice(letters))

# Voeg symbolen toe
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# Voeg nummers toe
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle de karakters in de password lijst
random.shuffle(password)

# Converteer de lijst naar een string
password_str = ''.join(password)

print(f"Hier is je wachtwoord: {password_str}")
