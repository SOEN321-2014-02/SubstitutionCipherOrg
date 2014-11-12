from guess import Guess
from monogrammatrix import MonogramMatrix

monoMatrixOfLanguageFrequencies = MonogramMatrix('erictest.txt')
monoMatrixOfLanguageFrequencies.setCharacterAsMostCommon(' ')

newGuess = Guess(monoMatrixOfLanguageFrequencies.getListOfUniqueCharacters())
newGuess.randomGuessOneCharacter()

monoMapping = monoMatrixOfLanguageFrequencies.generateMappingBasedOnFrequencies('text_pairs/1.ciphertext.txt')
newGuess.setGuess(monoMapping)
print(monoMapping)

#print(monoMatrixOfLanguageFrequencies.get())
#can do a bucket for dictionary?

