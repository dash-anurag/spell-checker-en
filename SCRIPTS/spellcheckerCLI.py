import sys

from spellchecker import SpellChecker

spell = SpellChecker()

print(spell.candidates(str(sys.argv[1])))
