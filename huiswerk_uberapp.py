# Definieer de beschikbare Uber opties als een lijst van tuples met naam en prijs per km
uber_opties = [("Uber X", 1.5), ("Uber Black", 2.0), ("Uber Van", 3.5)]
# Maak een lege lijst om de ritten in op te slaan
ritten = []

# Maak een dictionary om ritten per gebruiker op te slaan
userdict = {}

# Begin een oneindige lus om meerdere ritten toe te voegen
while True:
    current_user = input("Voer je gebruikersnaam in (of 'wissel' om van gebruiker te wisselen): ")
    
    if current_user.lower() == 'wissel':
        continue
    
    if current_user not in userdict:
        userdict[current_user] = []

    # Print de beschikbare Uber types en hun prijs per km
    print("Beschikbare Uber types:")
    for i in range(len(uber_opties)):
        # Toon de index, naam en prijs per km voor elke Uber optie
        print(f"{i + 1}: {uber_opties[i][0]} (€{uber_opties[i][1]} per km)")

    # Vraag de gebruiker om een Uber type te kiezen en zet de invoer om naar een index (keuze - 1)
    keuze = int(input("Kies een Uber type (nummer): ")) - 1
    # Vraag de gebruiker om het aantal kilometers van de rit
    kilometers = int(input("Hoeveel kilometers gaat u reizen? "))

    # Haal de gekozen Uber type en prijs per km op uit de lijst
    uber_type, prijs_per_km = uber_opties[keuze]
    # Bereken de totale kosten van de rit
    totale_kosten = prijs_per_km * kilometers
    # Voeg de rit toe aan de rittenlijst van de huidige gebruiker als een tuple van (Uber type, kilometers, totale kosten)
    userdict[current_user].append((uber_type, kilometers, totale_kosten))

    # Vraag de gebruiker of hij nog een rit wil toevoegen of van gebruiker wil wisselen
    doorgaan = input("Wilt u nog een rit toevoegen, van gebruiker wisselen, of stoppen? (ja/wissel/stop): ")

    # Als de gebruiker 'stop' invoert, breek dan uit de lus
    if doorgaan.lower() == 'stop':
        break



# Print een overzicht van alle ritten per gebruiker
print("\nOverzicht van alle ritten:")
for user, user_ritten in userdict.items():
    print(f"\nRitten voor gebruiker {user}:")
    for rit in user_ritten:
        # Toon het Uber type, aantal kilometers en de kosten voor elke rit
        print(f"{rit[0]} voor {rit[1]} km - Kosten: €{rit[2]:.2f}")
    # Bereken en print de totale kosten van alle ritten voor deze gebruiker
    print(f"Totale kosten voor {user}: €{sum(rit[2] for rit in user_ritten):.2f}")

# Bereken en print de totale kosten van alle ritten voor alle gebruikers samen
totale_kosten_alle_gebruikers = sum(sum(rit[2] for rit in ritten) for ritten in userdict.values())
print(f"\nTotale kosten voor alle gebruikers: €{totale_kosten_alle_gebruikers:.2f}")