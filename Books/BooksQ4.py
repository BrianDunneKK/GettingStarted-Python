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
            word_counter[word.lower()] += 1

    I_me = word_counter["I"] + word_counter["me"]
    you = word_counter["you"]
    he_him = word_counter["he"] + word_counter["him"]
    she_her = word_counter["she"] + word_counter["her"]
    print(f"Word usage: I/me = {I_me}, you = {you}, he/him = {he_him}, she/her = {she_her}\n")
    return(word_counter)

words = read_book("TheImportanceOfBeingEarnest")
words = read_book("TheAdventuresOfSherlockHolmes")
words = read_book("AliceInWonderland")
