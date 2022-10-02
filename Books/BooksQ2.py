
def read_book(book_name):
    print(f"\nReading the book {book_name}")
    with open(f"./Books/{book_name}.txt", encoding='utf-8') as f:
        all_lines = f.read().splitlines()

    all_words = {}
    total_words = 0
    total_characters = 0
    for line in all_lines:
        for word in line.split():
            total_words += 1
            total_characters += len(word)
            if word in all_words:
                all_words[word] += 1
            else:
                all_words[word] = 1

    print(f"It contains {total_words} words and {total_characters} letters.")
    print(f"It contains {len(all_words)} different words.\n")

read_book("TheImportanceOfBeingEarnest")
read_book("TheAdventuresOfSherlockHolmes")
read_book("AliceInWonderland")
