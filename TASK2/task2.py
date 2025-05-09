import urllib.request
import urllib.parse
import urllib.error
import json

serviceurl = "http://www.omdbapi.com/?"
apikey = "&apikey=1077504f" 

def print_json(data):
    print("-" * 20)
    info = [
        "Title", "Year", "Rated", "Released", "Runtime", "Genre", "Director",
        "Writer", "Actors", "Plot", "Language", "Country", "Awards",
        "Poster", "Ratings", "Metascore", "imdbRating", "imdbVotes",
        "imdbID", "Type", "DVD", "BoxOffice", "Production", "Website", "Response"
    ]
    for key in info:
        if key in data:
            if key == "Ratings":
                print(f"{key}: ")
                for rating in data.get('Ratings', []):
                    print(f"    - Source: {rating.get('Source')}, Value: {rating.get('Value')}")
            else:
                print(f"{key}: {data[key]}")
    print("-" * 20)

def save_poster(data):
    if 'Poster' in data and data['Poster'] != "N/A":
        poster_url = data['Poster']
        movie_title = data['Title'].replace(" ", "_").replace(":", "")
        filename = f"{movie_title}_poster_6609612061.jpg"
        try:
            with urllib.request.urlopen(poster_url) as response:
                poster_data = response.read()
            with open(filename, 'wb') as f:
                f.write(poster_data)
            print(f"Poster saved as {filename}")
        except Exception as e:
            print(f"Can't save poster: {e}")
    else:
        print("No poster available to download.")

def search_movie(title):
    try:
        title_url = urllib.parse.urlencode({'t': title})
        full_url = serviceurl + title_url + apikey
        with urllib.request.urlopen(full_url) as response:
            data = response.read().decode()
            json_data = json.loads(data)

            if json_data.get('Response', 'False') == 'True':
                print_json(json_data)
                save_poster(json_data)
                return json_data
            else:
                print("Error:", json_data.get('Error', 'Unknown error'))
                return None
    except Exception as e:
        print("Failed to retrieve data:", e)
        return None
    
title = input("Enter movie title: ")
search_movie(title)
