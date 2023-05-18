import nltk
import translators
nltk.download('punkt')

def translate_book(book_name, to_language):
    print(f"\nTranslating the book {book_name}")
    with open(f"./Books/{book_name}.txt", encoding='utf-8') as f:
        all_lines = f.read().splitlines()

    all_lines = ' '.join(all_lines)
    sentences = nltk.sent_tokenize(all_lines)

    for sentence in sentences:
        str = translators.translate_text(sentence, translator = 'google', to_language =  to_language)
        print(str)

translate_book("SimpleBook", to_language = 'ga')
translate_book("SimpleBook", to_language = 'fr')
# translate_book("TheImportanceOfBeingEarnest", to_language = 'ga')
# translate_book("TheAdventuresOfSherlockHolmes")
# translate_book("AliceInWonderland")
