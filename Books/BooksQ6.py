from collections import Counter
import re

def read_book(book_name):
    print(f"\nReading the book {book_name}")
    with open(f"./Books/{book_name}.txt", encoding='utf-8') as f:
        all_lines = f.read().splitlines()

    word_counter = Counter()
    for line in all_lines:
        for word in re.split('[ \!\"\&\*\(\)\-\_\=\+\,\.\?\<\>\;\:\'\@\#\~]', line):
            word_counter[word] += 1

    word_lengths = {key: len(key) for key, val in word_counter.items() }
    word_lengths_7up = {key: len(key) for key, val in word_counter.items() if len(key) >= 7 }
    word_count = len(word_lengths)
    word_count_7up = len(word_lengths_7up)
    perc_7up = word_count_7up*100.0/word_count
    print(f"There are {word_count} different words and {word_count_7up} ({perc_7up:.1f}%) of these have more than 7 letters")

    return(word_counter)

words = read_book("TheImportanceOfBeingEarnest")
words = read_book("TheAdventuresOfSherlockHolmes")
words = read_book("AliceInWonderland")
words = read_book("SimpleBook")
