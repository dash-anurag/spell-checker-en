from spellchecker import SpellChecker
import sys

spell = SpellChecker()

print(spell.candidates(str(sys.argv[1])))