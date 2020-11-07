from spellchecker import SpellChecker
import re

# creating spellchecker object
spell = SpellChecker(distance=2)

# creating file object
f = open("input.txt", 'r')

# importing contents of input.txt file into data
data = f.read()

# dividing the contents of input.txt file into list of sentences with the delimiters being "." and "\n"
sentences = re.split('; |, |\.|\n', data)

# removing empty list elements formed from the above operation
while "" in sentences:
    sentences.remove("")
# print(sentences)

# for loop for looping over the list of sentences
for sentence in sentences:
    # creating a temp list for storing the corrected words
    correct_word = []
    # using strip() to clear any white spaces from the list element and them splitting them into individual words
    words = sentence.strip().split(" ")
    # print(words)
    # applying the correction function from the pyspellchecker library and them adding them to the temp list
    for word in words:
        correct_word.append(spell.correction(word))
    # finally joining the individual words and displaying the correctly spelled words to form a sentence
    print(" ".join(correct_word) + ".")

# closing the file
f.close()
