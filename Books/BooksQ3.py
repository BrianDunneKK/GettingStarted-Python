from collections import Counter

def read_book(book_name):
    print(f"\nReading the book {book_name}")
    with open(f"./Books/{book_name}.txt", encoding='utf-8') as f:
        all_lines = f.read().splitlines()

    word_counter = Counter()
    total_characters = 0
    for line in all_lines:
        for word in line.split():
            total_characters += len(word)
            word_counter[word] += 1

    top10_str = ', '.join(map(lambda x: str(x[0]), word_counter.most_common(10)))
    print(f"It contains {word_counter.total()} words and {total_characters} letters.")
    print(f"It contains {len(word_counter)} different words.")
    print(f"The 10 most common words are: {top10_str}\n")
    return(word_counter)

words = read_book("TheImportanceOfBeingEarnest")
words = read_book("TheAdventuresOfSherlockHolmes")
words = read_book("AliceInWonderland")
