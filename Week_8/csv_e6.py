

import csv

def display_games_by_developer():
    game_developer= input("choose game developer: ")

    with open ("games.csv", 'r', encoding="utf-8") as file:

        read= csv.DictReader(file)
        for row in read:
            if row ["developer"] == game_developer:
                print(f"Name: {row['name']}")
                print(f"Genre: {row['genre']}")
                print(f"Developer: {row['developer']}")
                print(f"Rating: {row['rating']}")

display_games_by_developer()                