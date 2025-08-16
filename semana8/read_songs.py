

def read_songs():
    with open("songs.txt", "r") as file:
        lines= file.readlines()
        lines.sort()

    with open ("songs_sorted.txt", "w") as file2:
        for line in lines:
            file2.write(line.strip() + "\n")
read_songs()