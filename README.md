# spell-checker-en
We were given the task to design and implement a spell checker for web search and mining purposes. A Graphical User Interface is created in python using Tkinter . The input is given by the user in the form of a word or sentence or a group of sentences in the chatbox. The output is given in two forms for each identified misspelled word. One in the form of candidate words and other in the most probable word.

Steps to run the code locally:
1. Install Python3 in the system.
2. Install pyspellchecker. (Eg. in linux terminal type, `sudo pip install pyspellchecker`)
3. Download the gui.py from the repository.
4. Run `python gui.py` in the terminal.

PS: The pyspellchecker uses *Levenshtein Distance Algorithm* to find permutations within an edit distance of 2 from the original word. It then compares all permutations (insertions, deletions, replacements, and transpositions) to known words in a word frequency list. Those words that are found more often in the frequency list are more likely the correct results.

pyspellchecker supports multiple languages including English, Spanish, German, French, and Portuguese. Dictionaries were generated using the [FrequencyWords project](https://github.com/hermitdave/FrequencyWords) on GitHub.

pyspellchecker supports Python 3 and Python 2.7 but, as always, Python 3 is the preferred version!

pyspellchecker allows for the setting of the *Levenshtein Distance* to check. For longer words, it is highly recommended to use a distance of 1 and not the default 2.
