from spellchecker import SpellChecker
from pathlib import Path

susWords = []

def all_lower(my_list):
    return [x.lower() for x in my_list]

def no_marks(my_list):
    i = 0
    my_new_list = my_list
    for word in my_list:
        for char in word:
            if (char.isalpha() != True and char.isnumeric() != True ):
                my_new_list[i] = word.replace(char, '')
        i+=1

    return my_new_list

spell = SpellChecker()
f_path = Path(r"test.txt")


with open(f_path, 'r') as f_object:
    words = f_object.read().split()

print(words)

words = all_lower(words)
words = no_marks(words)

print(words)


for word in words:

    with open(f_path) as myFile:
        for num, line in enumerate(myFile, 1):
            if word in line:
                if (spell.correction(word) != word):
                    susWords.append(word)
                    print('"',word,'"','found at line:', num, ' , Did you mean ' ,end="-->")

                    # Get the one `most likely` answer
                    print('"', spell.correction(word) ,'"', end=' ')

                if (len(spell.candidates(word)) > 1):
                    # Get a list of `likely` options
                    print('Or may be in --> ',spell.candidates(word))


print(susWords)