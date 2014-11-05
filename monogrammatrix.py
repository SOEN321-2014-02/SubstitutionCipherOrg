__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'

class MonogramMatrix:
    def __init__(self, languageFileToBuildFrequencyMatrix):
        self.matrix = {}
        self.learn(languageFileToBuildFrequencyMatrix)

    #Arguments:
    #	languageFileToBuildFrequencyMatrix is an already opened, readable file object
    def learn(self, languageFileToBuildFrequencyMatrix):
        #read the file by breaking it down by line and then by character
        for line in languageFileToBuildFrequencyMatrix:
            for character in line:
                if character != '\n': #ignore new lines because we do not care about them
                    if character in self.matrix:
                        self.matrix[character] += 1
                    else:
                        self.matrix[character] = 1

    def addCharacterAsMostCommon(self, characterOfSeperator):
        self.matrix[characterOfSeperator] = 2*self.matrix[max(self.matrix, key=self.matrix.get)]

    def get(self):
        return self.matrix

    def getNumberOfUniqueCharacters(self):
        return len(self.matrix)