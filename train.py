import requests
import json
import numpy
import string
import time

start_time = time.perf_counter()
# Define the API endpoint and parameters
url = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "exlimit": 1,
    "explaintext": 1
}

# Define the User-Agent header
headers = {
    "User-Agent": "ChatbotDataScraper/1.0"
}

# Define the list of page titles
page_titles = ['United States', 'Donald Trump', 'Elizabeth II', 'India', 'Barack Obama', 'Christiano Ronaldo', 'World War II', 'United Kingdom', 'Michael Jackson', 'Elon Musk', 'Sex', 'Lady Gaga', 'Adolf Hitler', 'Eminem', 'Lionel Messi', 'Game of Thrones', 'World War I', 'The Beatles', 'Justin Bieber', 'Canada', 'Freddie Mercury', 'Kim Kardashian', 'Johnny Depp', 'Steven Jobs', 'Dwayne Johnson', 'Michael Jordan', 'Australia', 'List of presidents of the United States', 'The Big Bang Theory', 'Taylor Swift', 'Stephen Hawking', 'List of highest-grossing films', 'China', 'Russia', 'New York City', 'Japan', 'Kanye West', 'List of Marvel Cinematic Universe films', 'Abraham Lincoln', 'LeBron James', 'Charles III', 'Darth Vader', 'Star Wars', 'Miley Cyrus', 'Germany', 'September 11 attacks', 'Leonardo DiCaprio', 'Kobe Bryant', 'Selena Gomez', 'Joe Biden', 'Tom Cruise', 'Rihanna', 'Albert Einstein', 'Academy Awards', 'Prince Philip, Duke of Edinburgh', 'Harry Potter', 'Elvis Presley', 'The Walking Dead (TV series)', 'Scarlett Johansson', 'Lil Wayne', 'Tupac Shakur', 'Angelina Jolie', 'Queen Victoria', 'Jeffrey Dahmer', 'John F. Kennedy', 'COVID-19 pandemic', 'Diana, Princess of Wales', 'Marilyn Monroe', 'Keanu Reeves', 'Arnold Schwarzenegger', 'How I Met Your Mother', 'Chernobyl disaster', 'France', 'Ariana Grande', 'Jennifer Aniston', 'Breaking Bad', 'Meghan, Duchess of Sussex', 'Muhammed Ali', 'Will Smith', 'Ted Bundy', 'Pablo Escobar', 'Mila Kunis', 'Vietnam War', 'Mark Zuckerberg', 'Manchester United F.C.', 'William Shakespeare', 'Titanic', 'Tom Brady', 'Jay-Z', 'Singapore', 'Earth', 'Bill Gates', 'Winston Churchill', 'Bruce Lee', 'Nicki Minaj', 'Israel', 'Princess Margaret, Countess of Snowdon', 'John Cena', 'Charles Manson', 'Ryan Reynolds', 'Brad Pitt', 'Vladimir Putin']

# Define the list of letter distributions
letter_distribution = [0] * 26

# Iterate over the list of page titles and extract the text of each page
for title in page_titles:
    # Add the title parameter to the API query
    params["titles"] = title

    # Send the API request and parse the response
    response = requests.get(url, params=params, headers=headers, timeout=10)
    data = json.loads(response.text)

    # Extract the text of the page
    page_id = list(data["query"]["pages"].keys())[0]
    page_text = data["query"]["pages"][page_id]["extract"]

    # Add the letter counts for all letters to list
    for i in range(0, 26, 1):
        letter_distribution[i] += page_text.count(chr(i+65)) + page_text.count(chr(i+97))

char_count = sum(letter_distribution)
for i in range(26):
    letter_distribution[i] = letter_distribution[i] / char_count

letter_distribution = numpy.array(letter_distribution)
for i in range(500):
    print("".join(numpy.random.choice(list(string.ascii_lowercase), 5, p=letter_distribution)))

print()

end_time = time.perf_counter()

print(f"Program took {round(end_time - start_time, 3)} seconds to run")