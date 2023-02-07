from flask import Flask, render_template, request
from spellchecker import SpellChecker
from pathlib import Path

#a function to lowerCase all words
def all_lower(my_list):
    return [x.lower() for x in my_list]
#a finction to delete all kind chars expect letters and numbers
def no_marks(my_list):
    i = 0
    my_new_list = my_list
    for word in my_list:
        for char in word:
            if (char.isalpha() != True and char.isnumeric() != True ):
                my_new_list[i] = word.replace(char, '')
        i+=1

    return my_new_list

#initializes
spell = SpellChecker()
app = Flask(__name__)
lines = []
corrections = []
candidates = []
susWords = []


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["GET", "POST"])
def check():
    text=request.form['lol']
    words = text.split()

    words = all_lower(words)
    words = no_marks(words)
    susWords= spell.unknown(words)

    for word in susWords:
        corrections.append(spell.correction(word))
        candidates.append(spell.candidates(word))

    if words:
        return render_template("check.html", text=text, words=words, susWords=susWords, lines=lines, corrections=corrections, candidates=candidates)
    else:
        return render_template("failure.html")