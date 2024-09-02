
steden = ("Amsterdam", "Rotterdam", "Utrecht", "Den Haag", "Eindhoven", "Groningen")
# Loop door de tuple en print elk element afzonderlijk
for stad in steden:
    print(stad)


# --------------------------------------------------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Combineer de twee tuples tot één nieuwe tuple

tuple3 = tuple1 + tuple2
print(tuple3)
# --------------------------------------------------------------------------------------------


# Definieer een tuple met verschillende soorten gegevens (bijvoorbeeld getallen, strings, booleans, etc.)
tuplemix = ("hello world", 1, 2.5, True, (1, 2, 3), False)
index = 2
print(tuplemix[index])

# Print enkele elementen van de tuple namelijk het eerste, een subset (vanaf index 2 tot index 5) en het laatste element

start = 1
end = 4
print(tuplemix[start:end])

# --------------------------------------------------------------------------------------------


# Maak een tuple met een naam en een leeftijd
tuple_identity = ("Lars", 25)

# Pak de gegevens uit de tuple en sla ze op in afzonderlijke variabelen (Wat gebeurt er als je de variabelen in de verkeerde volgorde definieert?)


# Print de uitgepakte variabelen

