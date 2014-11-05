__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'

from random import randint

class Guess:
    def __init__(self, numberOfUniqueCharactersInLanguage):
        self.charactersInLanguage = numberOfUniqueCharactersInLanguage
        self.guessKey = []
        self.randomGuessAllCharacters()

    def setGuess(self, initialGuessMatrix):
        return 1

    def randomGuessAllCharacters(self):
        for i in range(0, self.charactersInLanguage):
            randomValue = randint(0, self.charactersInLanguage-1)

            #if this key value already exists in our list then we need to find a different one
            while self.guessKey.count(randomValue) > 0:
                randomValue = (randomValue + 1)%self.charactersInLanguage

            self.guessKey.append(randomValue)

    def randomGuessOneCharacter(self):
        #Make sure we have enough rows to swap first
        if len(self.guessKey) > 1:
            firstGuessRowToSwap = randint(0, self.charactersInLanguage-1)
            secondGuessRowToSwap = randint(0, self.charactersInLanguage-1)

            #do not swap a row with itself, try guessing until we get two unique rows to swap
            while secondGuessRowToSwap == firstGuessRowToSwap:
                secondGuessRowToSwap = (secondGuessRowToSwap + randint(0, self.charactersInLanguage-1))%self.charactersInLanguage

            self.__swapRows(firstGuessRowToSwap, secondGuessRowToSwap)

    def get(self):
        return self.guessKey

    def __swapRows(self, row1, row2):
        tempSwapVariable = self.guessKey[row1]
        self.guessKey[row1] = self.guessKey[row2]
        self.guessKey[row2] = tempSwapVariable