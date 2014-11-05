__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'

from random import randint

class Guess:
    def __init__(self, listOfUniqueCharactersInLanguage):
        self.uniqueCharactersInLanguage = len(listOfUniqueCharactersInLanguage)
        self.guessKey = {}
        self.listOfUniqueCharactersInLanguage = listOfUniqueCharactersInLanguage
        self.__buildOneToOneMappingOfCharacters()

    def setGuess(self, guessDictionary):
        self.guessKey =  guessDictionary

    def setListOfUniqueCharactersInLanguage(self, listOfUniqueCharactersInLanguage):
        self.uniqueCharactersInLanguage = len(listOfUniqueCharactersInLanguage)
        self.listOfUniqueCharactersInLanguage = listOfUniqueCharactersInLanguage

    def randomGuessAllCharacters(self):
        self.guessKey = {}
        for i in range(0, self.uniqueCharactersInLanguage):
            randomValue = randint(0, self.uniqueCharactersInLanguage-1)

            #if this key value already exists in our list then we need to find a different one
            while self.listOfUniqueCharactersInLanguage[randomValue] in self.guessKey.values():
                randomValue = (randomValue + 1)%self.uniqueCharactersInLanguage

            self.guessKey[self.listOfUniqueCharactersInLanguage[i]] = self.listOfUniqueCharactersInLanguage[randomValue]

    def randomGuessOneCharacter(self):
        #Make sure we have enough rows to swap first
        if len(self.guessKey) > 1:
            firstGuessRowToSwap = randint(0, self.uniqueCharactersInLanguage-1)
            secondGuessRowToSwap = randint(0, self.uniqueCharactersInLanguage-1)

            #do not swap a row with itself, try guessing until we get two unique rows to swap
            while secondGuessRowToSwap == firstGuessRowToSwap:
                secondGuessRowToSwap = (secondGuessRowToSwap + randint(0, self.uniqueCharactersInLanguage-1))%self.uniqueCharactersInLanguage

            self.__swapRows(firstGuessRowToSwap, secondGuessRowToSwap)

    def get(self):
        return self.guessKey

    def __swapRows(self, row1, row2):
        tempForSwap = self.guessKey[self.listOfUniqueCharactersInLanguage[row1]]
        self.guessKey[self.listOfUniqueCharactersInLanguage[row1]] = self.guessKey[self.listOfUniqueCharactersInLanguage[row2]]
        self.guessKey[self.listOfUniqueCharactersInLanguage[row2]] = tempForSwap

    def __buildOneToOneMappingOfCharacters(self):
        for character in self.listOfUniqueCharactersInLanguage:
            self.guessKey[character] = character