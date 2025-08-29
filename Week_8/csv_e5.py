

import csv

def count_games_by_genre():

    genre_count={}

    with open("games.csv", 'r', encoding="utf-8") as file:
        read= csv.DictReader(file)
        for row in read:
            genre = row["genre"]
            if genre in genre_count:
                genre_count[genre] +=1

            else:
                genre_count[genre] = 1   
    print ("Game count by Genre: ")

    for genre, count in genre_count.items():
        print (f"{genre}: {count}")             

count_games_by_genre()