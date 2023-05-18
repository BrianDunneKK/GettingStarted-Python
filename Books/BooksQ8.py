import nltk
nltk.download('punkt')

def read_book(book_name):
    print(f"\nReading the book {book_name}")
    with open(f"./Books/{book_name}.txt", encoding='utf-8') as f:
        all_lines = f.read().splitlines()

    all_lines = ' '.join(all_lines)
    sentences = nltk.sent_tokenize(all_lines)

    longest = ""
    for sentence in sentences:
        if len(longest) < len(sentence):
            longest = sentence

    print(longest)

read_book("TheImportanceOfBeingEarnest")
read_book("TheAdventuresOfSherlockHolmes")
read_book("AliceInWonderland")
