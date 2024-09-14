import requests
import random

# Constante waarden in hoofdletters
BASE_URL = "https://restcountries.com/v3.1/all"

# Parameters voor de API request om alleen de benodigde velden op te halen
PARAMS = {
    "fields": "name,region"
}

# Mogelijke regio's met bijbehorende cijfers
REGION_OPTIONS = {
    1: "Africa",
    2: "Americas",
    3: "Asia",
    4: "Europe",
    5: "Oceania",
    6: "Antarctic"
}

SCORE_FILE = "scores.txt"


def get_countries_data():
    """
    Haalt landeninformatie op van de API.
    """
    try:
        response = requests.get(BASE_URL, params=PARAMS)
        response.raise_for_status()
        countries = response.json()
        return countries
    except requests.exceptions.RequestException as e:
        print(f"Er is een fout opgetreden bij het ophalen van landeninformatie: {e}")
        return None


def play_guess_the_region_game(countries):
    """
    Spel waarbij je moet raden in welke regio een land ligt.
    """
    # Maak een lijst van landen met geldige regio's en namen
    valid_countries = [country for country in countries if 'region' in country and 'name' in country]

    score = 0  # Begin score

    while True:
        selected_country = random.choice(valid_countries)
        country_name = selected_country['name']['common']
        correct_region = selected_country['region']

        print(f"\nRaad de regio van het land: {country_name}")
        print("Mogelijke regio's:")
        for number, region in REGION_OPTIONS.items():
            print(f"{number}. {region}")

        # Vraag om een regio van de gebruiker door een cijfer in te voeren
        try:
            user_choice = int(input("Voer het nummer in van je keuze: "))
            user_guess = REGION_OPTIONS.get(user_choice, "").lower()
        except ValueError:
            user_guess = ""

        # Controleer of de gok correct is (hoofdletterongevoelig)
        if user_guess == correct_region.lower():
            score += 1
            print(f"Correct! Je huidige score is: {score}. Blijf doorgaan!")
        else:
            print(f"Helaas, fout. {country_name} ligt in de regio: {correct_region}.")
            print(f"Je eindscore is: {score}. Bedankt voor het spelen!")
            break  # Exit the loop instead of returning

    return score


def save_score(username, score):
    """Save user's score to file."""
    with open(SCORE_FILE, 'a') as file:
        file.write(f"{username},{score}\n")
    print(f"Score opgeslagen: {username}, {score}")

def display_scores():
    """    Print the contents of the scores.txt file."""
    with open(SCORE_FILE, 'r') as file:
        print("Contents of scores.txt:")
        print(file.read())

def main():
    """
    Voer het spel uit.
    """
    username = input("Wat is je naam? ")
    # Haal landeninformatie op
    countries = get_countries_data()
    if countries:
        # Start het spel
        score = play_guess_the_region_game(countries)
        save_score(username, score)
        display_scores()
    else:
        print("Kan het spel niet starten zonder landeninformatie.")


# Start het spel
if __name__ == "__main__":
    main()