from collections import Counter
import re

def read_book(book_name):
    print(f"\nReading the book {book_name}")
    with open(f"./Books/{book_name}.txt", encoding='utf-8') as f:
        all_lines = f.read().splitlines()

    word_counter = Counter()
    for line in all_lines:
        for word in re.split('[ !"&*()-_=+,.?<>;:\'@#~—]', line):
            word_counter[word] += 1

    word_lengths = {key: len(key) for key, val in word_counter.items() }
    word_lengths_top10 = Counter(word_lengths).most_common(10)
    longest10 = '\n'.join(map(lambda x: ' '+x[0], word_lengths_top10))
    print(f"The longest words in the book are:\n{longest10}")

    word_lengths = {key: len(key) for key, val in word_counter.items() if not key.endswith("ly") }
    word_lengths_top10 = Counter(word_lengths).most_common(10)
    longest10 = '\n'.join(map(lambda x: ' '+x[0], word_lengths_top10))
    print(f"\nThe longest words that don't end in 'ly' are:\n{longest10}")

    return(word_counter)

words = read_book("TheImportanceOfBeingEarnest")
words = read_book("TheAdventuresOfSherlockHolmes")
words = read_book("AliceInWonderland")
