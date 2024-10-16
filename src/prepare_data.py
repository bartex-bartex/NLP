import re

with open('book.txt', 'r', encoding='utf-8') as f:
    book = f.read()

book = re.sub(r'\*\s?\(\d+\)', '', book)
book = re.sub(r'\s+', ' ', book)
book = re.sub(r'[,.!?*"“”;:()]', '', book)

with open('book.txt', 'w', encoding='utf-8') as f:
    f.write(book)