from spellchecker import SpellChecker

spell = SpellChecker()

# misspelled = spell.unknown(['let', 'us', 'wlak', 'on', 'the', 'groun'])
#
# for word in misspelled:
#     print(spell.correction(word))
#
#     print(spell.candidates(word))

f = open("input.txt", 'r')
data = f.read()
sentences = data.split("\n")
for sentence in sentences:
    correct_sentence = []
    words = sentence.split(" ")
    # print(words)
    for word in words:
        correct_sentence.append(spell.correction(word))
    print(" ".join(correct_sentence))
f.close()
