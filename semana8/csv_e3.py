
import csv

def read_games():
    with open('games.csv', 'r', encoding='utf-8') as file:
        game_info= csv.DictReader(file)
        for row in game_info:
            print(row)

read_games()        