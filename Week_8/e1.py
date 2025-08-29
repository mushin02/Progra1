
import csv

def write_games_CSV(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer= csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


number_of_games= int(input("How many games do you want to enter? "))

video_game_library = []


for num in range(number_of_games):
    name= input("Name: ")
    genre= input("Genre: ")
    developer= input("Developer: ")
    rating= input("Rating: ")

    video_game_library.append({
        "name": name,
        "genre": genre,
        "developer": developer,
        "rating": rating
    })

write_games_CSV('games.csv', video_game_library, ["name", "genre", "developer", "rating"])