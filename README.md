# Spell-Checker-Website
A spell checker web application built on Flask, a framework of python
# Spell Checker Website
#### Video Demo: https://youtu.be/aw-v3qT-lCs
##### Description: The app.py program uses the flask library to run the Web pages on flask server, and uses the spellchecker library to import a function from it named SpellChecker() in order to use it check the spelling of each word it takes, then we have two functions I defined which are all_lower() that converts each word in a list of words it takes to lower cases words only, And no_marks() that deletes every non alphabetical or numerical character in every word  in a list such as dots, commas, hashtags, etc.. , then we define the SpellChecker() function as spell for simplicity, and the Flask() function that takes the (name) argument as app, and then we declare three empty lists which are corrections, candidates, susWords, and then for the first route it's relly simple it's just the default route ("/") and we will display in that case the index.html file, and then the second route ("/check") which has the algorithm for which we test the spelling of the words, first we get the text message from the user using POST and store in variable called text which will be a whole string, and then, using the split() function we split the text string into a list of strings and declare it as words which is a list of strings, then we use the all_lower() and the no_marks() functions which we defined earlier to change each word in the words list into an all lower case words with no symbols, the we get each all words that have a wrong spelling and store it in a list called susWords, and the we iterate over each word of the words list and for each word we get the correction of the spelling of it and store in the corrections list, and a list of other candidates of the correction of the word and store in the candidates list, and then if the words list was empty all tht time meaning the user inputed nothing, then flask will display the failure.html file, other than that meaning if the words list isn't empty, then flask will display the check.html and passes to it the text string and the words list and the susWords list and the corrections list and the candidates list of lists, and the for our templates (the HTML files), in the templates directory we will find layout.html which will be extended in all our other templates, first we notice some links to bootstrap stylesheets and then at line 15 we notice a link to my own stylesheet at static/style.css, and then we have sompe javaScript script which will be used later in index.html, basically it changes the color of two buttons based on if it's a correct or wrong button, and also shows a hidden text for each button, and then we have the body tag that we have body block variable in it in jinja text, for index.html we firstly have a simple navigation bar, and then the first section in the page which is the about me section, and the the second section we have the checking section which has a simple form which submitting it will redirect us to ("/check"), and then the third section is a fun quiz I made just for fun and also to use my javaScript skills on it, it has a simple question and clicking the correct button will change it to green, and clicking the wrong button will change to red, nd a text will appear to help you choose the correct answer, and the fourth section which is the contact section, it has four cards each of them dispalys a way of contacting me, phone number, e-mail, Facebook and LinkedIn which both have direct link to my profile on both, hovering over each of them will make them get bigger smoothly, and at last we have the footer which has the copyrights message and my name, next is the check.html file first div will display the original text the user inputed to check plus the wrong words in that text through jinja syntax, second text will display each wrong word with it's most likely correction and other candidates of the correction of that word, and lastely the failure.html file which just dispalys a message that indicatesvto the user that he didn't input a valid input, and in the static/ directory you will find only style.css which has -almost- all the styling for our html files especially the index.html, and lastly wewill find spellChecker.py and test.txt which were used as a prototype for my algorithm of the spell checking which we used in app.py, for in further questions or advices, contact me at ejrgfjg@gmail.com , Thanks for reading.
