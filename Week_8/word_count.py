
def count_words():

    with open("words.txt", "r") as file:
        text= file.read()
        words = text.split()
        return len(words)

print(f' This file has {count_words()} words')
 