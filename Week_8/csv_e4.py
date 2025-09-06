
import csv

def categorize_games():
    category_to_display= input("What category do you want to see? ")

    with open("games.csv", 'r', encoding='utf-8') as file:
        read = csv.DictReader(file)

        for row in read:
            if row ["rating"] == category_to_display:
                print(f"Name: {row['name']}")
                print(f"Genre: {row['genre']}")
                print(f"Developer: {row['developer']}")
                print(f"Rating: {row['rating']}")

categorize_games()            