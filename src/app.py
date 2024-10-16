import json
import spacy

nlp = spacy.load('en_core_web_sm')

def is_noun(word):
    doc = nlp(word)
    return doc[0].pos_ == 'NOUN' and doc[0].pos_ != 'PROPN'

def get_base_form(word):
    doc = nlp(word)
    return doc[0].lemma_

nouns_by_verb = {}

# verbs
with open('data/verbs.json', 'r') as f:
    verbs = json.load(f)

# articles
with open('data/articles.json', 'r') as f:
    articles = json.load(f)["articles"]

# Title: War and Peace | 566328 words
with open('data/book.txt', 'r', encoding='utf-8') as f:
    book = f.read()

words = book.split()

i = 0
while i < len(words) - 1:
    word = words[i]
    if word in articles:
        i += 1
        continue
    for verb_key, verb_forms in verbs.items():
        if word in verb_forms:

            # grab the next word
            next_word = words[i+1]
            i += 1

            # skip articles
            while next_word in articles:
                if i + 1 >= len(words):
                    next_word = None
                    break

                next_word = words[i+1]
                i += 1

            # add to dictionary
            if next_word and is_noun(next_word):
                next_word = get_base_form(next_word)
                nouns_by_verb.setdefault(verb_key, set()).add(next_word)
            
            break
    i += 1

nouns_by_verb = {key: list(value) for key, value in nouns_by_verb.items()}

with open('output/output.json', 'w', encoding='utf-8') as f:
    json.dump(nouns_by_verb, f, ensure_ascii=False, indent=4)