__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'

import re

class AccuracyOfDecryption:
    def __init__(self, filenameContainingLanguageWordList):
        self.dictionaryBucket = {}
        self.__loadWordListFromFile(filenameContainingLanguageWordList)

    def __loadWordListFromFile(self, filenameContainingLanguageWordList):
        with open(filenameContainingLanguageWordList, 'r') as wordListFile:
            for line in wordListFile:
                wordsInLine = []
                wordsInLine.extend(re.split('\s',line))
                for currentWord in wordsInLine:
                    currentWord = currentWord.lower()
                    if len(currentWord) > 0:
                        firstLetter = currentWord[0]
                        if not(firstLetter in self.dictionaryBucket.keys()):
                            self.dictionaryBucket[firstLetter] = []

                        self.dictionaryBucket[firstLetter].append(currentWord)

    def getCountOfAccurateWords(self, decryptedText):
        countOfAccurateWords = 0

        whitespaceSeperatedDecryptedText = re.split('\s', decryptedText)

        for currentWord in whitespaceSeperatedDecryptedText:
            currentWord = currentWord.lower()
            currentWordLength = len(currentWord)
            if currentWordLength > 0:
                if currentWord in self.dictionaryBucket[currentWord[0]]:
                    countOfAccurateWords += 1

        return countOfAccurateWords

    def getCountOfAccurateWordsByLength(self, decryptedText):
        accurateWordsByLength = {}

        whitespaceSeperatedDecryptedText = re.split('\s', decryptedText)

        for currentWord in whitespaceSeperatedDecryptedText:
            currentWord = currentWord.lower()
            currentWordLength = len(currentWord)
            if currentWordLength > 0:
                if currentWord in self.dictionaryBucket[currentWord[0]]:
                    if currentWordLength in accurateWordsByLength.keys():
                        accurateWordsByLength[currentWordLength][0] += 1
                    else:
                        accurateWordsByLength[currentWordLength] = [1, 0]
                accurateWordsByLength[currentWordLength][1] += 1

        return accurateWordsByLength

    def getAccuracyPercentage(self, decryptedText):
        return (self.getCountOfAccurateWords(self, decryptedText)/len(re.split('\s', decryptedText)))*100
