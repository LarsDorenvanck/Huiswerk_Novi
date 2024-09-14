import requests

def get_coordinates(city_name):
    url = f'https://nominatim.openstreetmap.org/search?q={city_name}&format=json'
    headers = {'User-Agent': 'YourAppName/1.0'}  # Add a User-Agent header
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        else:
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_population(city_name, username):
    url = f'http://api.geonames.org/searchJSON?q={city_name}&maxRows=1&username={username}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'geonames' in data and len(data['geonames']) > 0:
            return data['geonames'][0]['population']
        else:
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    city = input("Enter a city name: ")
    coords = get_coordinates(city)
    if coords:
        print(f'Coordinates of {city}: {coords}')
    else:
        print(f'Could not find coordinates for {city}')
    
    username = 'lars_bela'  # Register for a free username
    population = get_population(city, username)
    if population:
        print(f'Population of {city}: {population}')
    else:
        print(f'Could not find population for {city}')

if __name__ == "__main__":
    main()
