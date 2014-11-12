from guess import Guess
from monogrammatrix import MonogramMatrix

mono = MonogramMatrix()
mono.learn_from_file('erictest.txt')
mono.setCharacterAsMostCommon(' ')

newGuess = Guess(mono.getListOfUniqueCharacters())
newGuess.randomGuessOneCharacter()

monoMapping = mono.generateMappingBasedOnFrequencies('text_pairs/1.ciphertext.txt')
newGuess.setGuess(monoMapping)
print(monoMapping)

#print(monoMatrixOfLanguageFrequencies.get())
#can do a bucket for dictionary?

