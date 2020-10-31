# spell-checker-en
We were given the task to design and implement a spell checker for web search and mining purposes. A pseudo database is created in python of misspelled words and is then fed to the spellchecker. The output consists a list of probable words that the user can select to replace the weong spelled word.

Steps to Implement the Code:
1. Intall Python3 in the system.
2. install pyspellchecker. (Eg. in linux terminal type, sudo pip install pyspellchecker.)
3. Dowload the script.py from the repository.
4. run python script.py in the terminal.

PS: The pyspellchecker uses a Levenshtein Distance algorithm to find permutations within an edit distance of 2 from the original word. It then compares all permutations (insertions, deletions, replacements, and transpositions) to known words in a word frequency list. Those words that are found more often in the frequency list are more likely the correct results.

pyspellchecker supports multiple languages including English, Spanish, German, French, and Portuguese. Dictionaries were generated using the WordFrequency project on GitHub.

pyspellchecker supports Python 3 and Python 2.7 but, as always, Python 3 is the preferred version!

pyspellchecker allows for the setting of the Levenshtein Distance to check. For longer words, it is highly recommended to use a distance of 1 and not the default 2.
