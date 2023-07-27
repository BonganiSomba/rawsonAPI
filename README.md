# rawsonAPI
Home Test 
The Lord of the Rings API Interaction
This repository contains a Python script that interacts with "The One API" to perform various tasks related to "The Lord of the Rings" movies and characters. The script uses the requests library to make HTTP requests to the API and fetches data in JSON format.

Requirements
To run the script, you need the following:

Python 3.x installed on your system.
The requests library installed. You can install it using pip:
Copy code
pip install requests
An API key from "The One API" to authenticate your requests. You can obtain the API key from the official documentation.
How to Use
Clone the repository to your local machine:

git clone https://github.com/BonganiSomba/lotr-api-interaction.git

cd lotr-api-interaction
Replace 'API_KEY' with your actual API key in the script. Open the lotr_api_interaction.py file in a text editor and locate the line:
python

headers = {'Authorization': 'Bearer API_KEY'}
Replace 'API_KEY' with your API key obtained from "The One API" documentation.

Run the script:

python lotr_api_interaction.py
The script will prompt you to choose from various tasks related to "The Lord of the Rings" movies and characters. Follow the instructions on the screen to interact with the API and retrieve information.

Tasks
Task 1: Retrieve Character Information
Enter the name of a character from "The Lord of the Rings" universe, and the script will use the API to fetch the character's information, including name, race, gender, birth, and death. The retrieved information will be displayed in a user-friendly format.

Task 2: Fetch a Random Quote from "The Lord of the Rings" Movies
The script will retrieve a random quote from any of "The Lord of the Rings" movies. It will display the quote, the movie in which it was said, and the character who said it.

Task 3: Search Characters by Race
Enter the race of characters you want to search for, and the script will display all characters belonging to that race.

Task 4: Data Manipulation
The script will retrieve information about the characters and their appearances in movies from the API. It will then perform data manipulation to find out which character appears in the most movies and how many times.

Troubleshooting
If you encounter any issues or errors while running the script, double-check that you have replaced 'YOUR_API_KEY' with your actual API key. Also, ensure that you have installed the requests library as described in the Requirements section.

If you still face any problems, please feel free to create an issue on this GitHub repository, and we will be happy to assist you.


License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code according to the terms of the license.
