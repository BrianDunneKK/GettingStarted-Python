book = "TheImportanceOfBeingEarnest"
with open(f"./Books/{book}.txt", encoding='utf-8') as f:
    all_lines = f.read().splitlines()
print(f"The book {book} contains {len(all_lines)} lines.")
