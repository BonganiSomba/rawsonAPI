import requests
import random
import time

def get_character_info(character_name):
    url = f'https://the-one-api.dev/v2/character'
    headers = {'Authorization': 'Bearer 0F1IuybnwwTTjpw0OmE2'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['docs']
        for character in data:
            if character['name'].lower() == character_name.lower():
                return character
        return None
    else:
        print(f"Failed to get character data. Code: {response.status_code}")
        return None

def display_character_info(character_info):
    if character_info:
        print(f"Name: {character_info['name']}")
        print(f"Race: {character_info['race']}")
        print(f"Gender: {character_info['gender']}")
        print(f"Birth: {character_info['birth']}")
        print(f"Death: {character_info['death']}")
    else:
        print("Character not found.")

def get_movie_info(movie_id):
    url = f'https://the-one-api.dev/v2/movie/{movie_id}'
    headers = {'Authorization': 'Bearer 0F1IuybnwwTTjpw0OmE2'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        print(f"Failed to get movie data. Code: {response.status_code}")
        return None

def get_character_name(character_id):
    url = f'https://the-one-api.dev/v2/character/{character_id}'
    headers = {'Authorization': 'Bearer 0F1IuybnwwTTjpw0OmE2'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        character_data = response.json()
        character_name = character_data['docs'][0]['name'] if 'docs' in character_data and len(character_data['docs']) > 0 else None
        return character_name
    else:
        print(f"Failed to get character data. Code: {response.status_code}")
        return None

def get_random_movie_quote():
    url = 'https://the-one-api.dev/v2/quote'
    headers = {'Authorization': 'Bearer 0F1IuybnwwTTjpw0OmE2'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['docs']
        quote_info = random.choice(data)
        movie_id = quote_info['movie']
        character_id = quote_info['character']

        # Fetch movie name using movie_id directly
        movie_info = get_movie_info(movie_id)
        movie_name = movie_info.get('name', 'Unknown Movie')

        # Fetch character name
        character_name = get_character_name(character_id)

        if character_name:
            quote_info['movie'] = movie_name
            quote_info['character'] = character_name
            return quote_info
        else:
            return None
    else:
        print(f"Failed to get quote. Code: {response.status_code}")
        return None

def display_movie_quote(quote_info):
    if quote_info:
        print(f"Movie: {quote_info['movie']}")
        print(f"Character: {quote_info['character']}")
        print(f"Quote: {quote_info['dialog']}")
    else:
        print("Quote not found.")

def get_characters_by_race(race):
    url = f'https://the-one-api.dev/v2/character'
    headers = {'Authorization': 'Bearer 0F1IuybnwwTTjpw0OmE2'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['docs']
        characters_of_race = [character['name'] for character in data if character['race'].lower() == race.lower()]
        return characters_of_race
    else:
        print(f"Failed to get character data. Code: {response.status_code}")
        return None

def display_characters_by_race(characters, race):
    if characters:
        print(f"Characters belonging to race '{race}':")
        for character in characters:
            print(character)
    else:
        print(f"No characters found for the specified race '{race}'.")

def get_characters_and_appearances():
    url = 'https://the-one-api.dev/v2/quote'
    headers = {'Authorization': 'Bearer 0F1IuybnwwTTjpw0OmE2'}

    response = requests.get(url, headers=headers)

    # Retry mechanism
    retries = 3
    while response.status_code == 429 and retries > 0:
        print("Too many requests. Retrying after a short delay...")
        time.sleep(2)  # Wait for 2 seconds before retrying
        response = requests.get(url, headers=headers)
        retries -= 1

    if response.status_code == 200:
        data = response.json()['docs']
        characters_info = {}

        for quote_info in data:
            character_id = quote_info['character']
            character_name = get_character_name(character_id)
            if character_name:
                if character_name not in characters_info:
                    characters_info[character_name] = 1
                else:
                    characters_info[character_name] += 1

        return characters_info
    else:
        print(f"Failed to get quote data. Code: {response.status_code}")
        return None

def get_character_with_most_appearances(characters_info):
    if characters_info:
        most_appearances = max(characters_info.values())
        character_with_most_appearances = [character for character, appearances in characters_info.items() if appearances == most_appearances]
        return character_with_most_appearances, most_appearances
    else:
        return None, None

def main():
    options = ['Task 1: Retrieve Character Information',
               'Task 2: Fetch a Random Quote from "The Lord of the Rings" Movies',
               'Task 3: Search Characters by Race',
               'Task 4: Data Manipulation',
               'Exit']

    while True:
        print("\nSelect a task (enter the task number):")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = input()

        if choice == '1':
            # Task 1: Retrieve Character Information
            character_name = input("Enter the name of a character from 'The Lord of the Rings': ")
            character_info = get_character_info(character_name)
            display_character_info(character_info)

        elif choice == '2':
            # Task 2: Fetch a Random Quote
            quote_info = get_random_movie_quote()
            display_movie_quote(quote_info)

        elif choice == '3':
            # Task 3: Search Characters by Race
            race = input("Enter the race of characters to search for: ")
            characters = get_characters_by_race(race)
            display_characters_by_race(characters, race)

        elif choice == '4':
            # Task 4: Data Manipulation
            characters_info = get_characters_and_appearances()
            character_with_most_appearances, most_appearances = get_character_with_most_appearances(characters_info)

            if character_with_most_appearances and most_appearances:
                print(f"The character with the most appearances is: {character_with_most_appearances[0]}")
                print(f"Number of appearances: {most_appearances}")
            else:
                print("No character data available or an error occurred during data retrieval.")

        elif choice.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid task or type 'exit' to quit.")

if __name__ == "__main__":
    main()

