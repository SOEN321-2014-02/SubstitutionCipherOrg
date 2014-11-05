__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'

class MonogramMatrix:
    #Arguments:
    #	languageFileToBuildFrequencyMatrix is an already opened, readable file object
    def __init__(self, languageFileToBuildFrequencyMatrix):
        self.matrix = {}
        self.learn(languageFileToBuildFrequencyMatrix)

    #Arguments:
    #	languageFileToBuildFrequencyMatrix is an already opened, readable file object
    def learn(self, languageFileToBuildFrequencyMatrix):
        #read the file by breaking it down by line
        for line in languageFileToBuildFrequencyMatrix:
            #now break the line down into individual characters
            for character in line:
                #ignore new lines because we do not care about them
                if character != '\n':
                    if character in self.matrix:
                        self.matrix[character] += 1
                    else:
                        self.matrix[character] = 1

    def setCharacterAsMostCommon(self, characterToMakeMostCommon):
        #Finds the highest value in the dictionary, multiplies it by 2 and then sets the given character to this value
        self.matrix[characterToMakeMostCommon] = 2*self.matrix[max(self.matrix, key=self.matrix.get)]

    def get(self):
        return self.matrix

    def getListOfUniqueCharacters(self):
        listOfUniqueCharacters = []
        for key in self.matrix.keys():
            listOfUniqueCharacters.append(key)
        return listOfUniqueCharacters