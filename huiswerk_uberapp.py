# Gebruiker kiest het type Uber
print("Kies het type Uber:")
print("1: Uber X (€1,5 per km)")
print("2: Uber Black (€2,0 per km)")
print("3: Uber Van (€3,5 per km)")
keuze = int(input("Voer het nummer in van de gekozen Uber: "))

# Initialisatie van variabelen
uber_type = None
sfadfasdf = None



# Bepaal de prijs per kilometer op basis van de keuze
if keuze == 1:
    sfadfasdf = 1.5
    uber_type = "Uber X"
elif keuze == 2:
    sfadfasdf = 2.0
    uber_type = "Uber Black"
elif keuze == 3:
    sfadfasdf = 3.5
    uber_type = "Uber Van"
else:
    print("Ongeldige keuze")

# Gebruiker voert het aantal kilometers in
kilometers = int(input("Voer het aantal kilometers in: "))

# Bereken de totale kosten
totale_kosten = sfadfasdf * kilometers

# Geef de keuze en de kosten weer
print(f"Je hebt gekozen voor {uber_type} voor een afstand van {kilometers} km.")
print(f"De totale kosten zijn: €{totale_kosten:.2f}")
