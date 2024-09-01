# Gebruiker kiest het type Uber
print("Kies het type Uber:")
print("1: Uber X (€1,5 per km)")
print("2: Uber Black (€2,0 per km)")
print("3: Uber Van (€3,5 per km)")
keuze = int(input("Voer het nummer in van de gekozen Uber: "))

# Gebruiker voert het aantal kilometers in
kilometers = int(input("Voer het aantal kilometers in: "))
prijs = 0

if(keuze == 1):
    prijs = kilometers * 1.5
elif(keuze == 2):
    prijs = kilometers * 2
elif(keuze == 3):
    prijs = kilometers * 3.5
else:
    print("niet geldige keuze")
    exit()

#print output
print(f"De totale kosten zijn: {prijs} " "euro")

