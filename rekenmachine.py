from msilib import add_tables

# Schrijf een simpele rekenmachine. De gebruiker moet twee getallen en een operatie invoeren.
# Het programma moet de berekening uitvoeren en het resultaat printen.


getal_1 = float(input("input 1st number: "))
operator = input("input operator: ")
getal_2 = float(input("input 2nd number: "))

#result = eval(getal_1 + operator + getal_2)
#print (f"{getal_1} {operator} {getal_2} = {result}")

if operator == "+":
    result = getal_1 + getal_2
    print(f"{result}")
elif operator == "-":
    result = getal_1 - getal_2
    print(f"{result}")
elif operator == "*":
    result = getal_1 * getal_2
    print(f"{result}")
elif operator == "/":
    if getal_2 != 0:
        result = getal_1 / getal_2
        print(f"{result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")







# Voorbeeld:
# Enter the first number: 5.1
# Enter the second number: 3
# Enter the operation: +
# The result is: 8.1

# Het programma moet de volgende operaties ondersteunen: +, -, *, /
# Als de gebruiker een ongeldige operatie invoert, moet het programma "Invalid operation" printen.

