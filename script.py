from spellchecker import SpellChecker

spell = SpellChecker(distance=1)


misspelled = spell.unknown(['let', 'us', 'wlak','on','the','groun'])

for word in misspelled:
    
    print(spell.correction(word))

    
    print(spell.candidates(word))
