from guess import Guess
from monogrammatrix import MonogramMatrix
from accuracyofdecryption import AccuracyOfDecryption

mono = MonogramMatrix()
mono.learn_from_file('training_corpora/english_word_list.txt')
mono.setCharacterAsMostCommon(' ')

newGuess = Guess(mono.getListOfUniqueCharacters())
newGuess.randomGuessOneCharacter()

#monoMapping = mono.generateMappingBasedOnFrequencies('text_pairs/1.ciphertext.txt')
#newGuess.setGuess(monoMapping)
#print(monoMapping)

accOfDec = AccuracyOfDecryption('training_corpora/english_word_list.txt')
accurateResultsCount = accOfDec.getCountOfAccurateWords('hi my name is eric shady\ncats\tare what?  I taught eminem')
print(accurateResultsCount)

#print(monoMatrixOfLanguageFrequencies.get())
#can do a bucket for dictionary?

