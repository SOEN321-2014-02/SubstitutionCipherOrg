from guess import Guess
from monogrammatrix import MonogramMatrix

f = open('erictest.txt','r')
mmat = MonogramMatrix(f)
#mmat.addCharacterAsMostCommon(' ')

newGuess = Guess(mmat.getListOfUniqueCharacters())
newGuess.randomGuessOneCharacter()

print(newGuess.get())