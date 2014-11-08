from guess import Guess
from monogrammatrix import MonogramMatrix

mmat = MonogramMatrix('erictest.txt')
#mmat.addCharacterAsMostCommon(' ')

newGuess = Guess(mmat.getListOfUniqueCharacters())
newGuess.randomGuessOneCharacter()

print(mmat.get())