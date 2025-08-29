
import csv

video_game_library = [
    {
        "name": "Apex Legends",
        "genre": "Battle Royale",
        "developer": "Respawn Entertainment",
        "rating": "T"
    },
    {
        "name": "Call of Duty",
        "genre": "First-Person Shooter",
        "developer": "Activision",
        "rating": "M"
    },
    {
        "name": "God of War",
        "genre": "Action-Adventure",
        "developer": "Santa Monica Studio",
        "rating": "M"
    }
]




def write_games_CSV(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer= csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


write_games_CSV('games.csv', video_game_library, video_game_library[0].keys())