from collections import Counter
import re

def read_book(book_name):
    print(f"\nReading the book {book_name}")
    with open(f"./Books/{book_name}.txt", encoding='utf-8') as f:
        all_lines = f.read().splitlines()

    letter_counter = Counter()
    for line in all_lines:
        for letter in re.findall('[a-zA-Z]', line):
            letter_counter[letter.lower()] += 1

    letter_freq = [l for (l,x) in letter_counter.most_common()]
    print("".join(letter_freq))

    return(letter_counter)

letters = read_book("TheImportanceOfBeingEarnest")
letters = read_book("TheAdventuresOfSherlockHolmes")
letters = read_book("AliceInWonderland")
letters = read_book("SimpleBook")
