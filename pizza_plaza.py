# Je werkt in een pizzaria, en je moet een programma schrijven dat de kosten van een pizza berekent.
# Er zijn 3 maten pizza's Small (s), Medium (m) en Large (l).
# Een kleine pizza kost $15, een medium pizza kost $20 en een grote pizza kost $25.
# Als de klant extra pepperoni wil, kost dit $2 voor een kleine pizza en $3 voor een medium of grote pizza.
# Als de klant extra kaas wilt, dan kost dit $1.

size = input("Enter size of pizza: klein, medium, groot")
extra_pep = input("Enter extra pepperoni, True/False")
extra_kaas = input("Enter extra kaas, True/False")

base_price = 15
pep_price = 2
kaas_price = 1

if size == "klein":
    base_price = 15
elif size == "medium":
    base_price = 20
    pep_price = 3
elif size == "groot":
    base_price = 25
    pep_price = 3

base_price = float(base_price)
pep_price = float(pep_price)
kaas_price = float(kaas_price)

if extra_kaas == "False" and extra_pep == "False":
    print(base_price)
elif extra_kaas == "True" and extra_pep == "False":
    print(base_price+kaas_price)
elif extra_kaas == "False" and extra_pep == "True":
    print(base_price+pep_price)
elif extra_kaas == "True" and extra_pep == "True":
    print(base_price+kaas_price+pep_price)
