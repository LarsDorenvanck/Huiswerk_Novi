#CODE NOT IN USE
#CODE NOT IN USE
#CODE NOT IN USE

import random
import requests

def get_random_cities(num_cities):
    """
    Fetch a list of random capital cities from the RestCountries API.

    This function retrieves a list of countries from the RestCountries API,
    filters for countries with capital cities, and then randomly selects
    a specified number of capital cities from this filtered list.

    Args:
        num_cities (int): The number of random capital cities to return.

    Returns:
        list: A list of randomly selected capital city names.
        None: If there was an error fetching data from the API.

    Raises:
        requests.RequestException: If there's an error with the API request.
    """
    # RestCountries API endpoint
    base_url = "https://restcountries.com/v3.1/all"

    try:
        # Make the API request
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for bad responses
        countries = response.json()
        
        # Filter countries with capital cities
        countries_with_capitals = []
        for country in countries:
            if 'capital' in country and country['capital']:
                countries_with_capitals.append(country)
        
        # Select random countries
        random_countries = random.sample(countries_with_capitals, min(num_cities, len(countries_with_capitals)))
        
        # Get the capital cities of the random countries
        random_cities = [country['capital'][0] for country in random_countries]
        
        return random_cities

    except requests.RequestException as e:
        print(f"Error fetching data from RestCountries API: {e}")
        return None

if __name__ == "__main__":
    num_cities = 5  # You can change this number or get it from user input
    random_cities = get_random_cities(num_cities)
    if random_cities:
        print(f"Random cities selected: {', '.join(random_cities)}")
    else:
        print("Failed to get random cities.")
