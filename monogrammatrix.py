__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'

class MonogramMatrix:
    #Arguments:
    #	filenameToBuildFrequencyMatrix is a string representing the filename to use for building the matrix
    def __init__(self, filenameToBuildFrequencyMatrix):
        self.matrix = {}
        self.__learn(filenameToBuildFrequencyMatrix)

    def __learn(self, filenameToBuildFrequencyMatrix):
        with open(filenameToBuildFrequencyMatrix,'r') as languageFileToBuildFrequencyMatrix:
            #read the file by breaking it down by line
            for line in languageFileToBuildFrequencyMatrix:
                #treat upper and lower case characters as the same
                line = line.lower()
                #now break the line down into individual characters
                for character in line:
                    #ignore new lines because we do not care about them
                    if character != '\n':
                        if character in self.matrix:
                            self.matrix[character] += 1
                        else:
                            self.matrix[character] = 1

    def learn(self, text):
        for character in text:
            if character in self.matrix:
                self.matrix[character] += 1
            else:
                self.matrix[character] = 1

    def get_decreasing_vector(self):
        return sorted(self.matrix, key=self.matrix.get)

    def setCharacterAsMostCommon(self, characterToMakeMostCommon):
        characterToMakeMostCommon = characterToMakeMostCommon.lower
        #Finds the highest value in the dictionary, multiplies it by 2 and then sets the given character to this value
        self.matrix[characterToMakeMostCommon] = 2*self.matrix[max(self.matrix, key=self.matrix.get)]

    def get(self):
        return self.matrix

    def getListOfUniqueCharacters(self):
        listOfUniqueCharacters = []
        for key in self.matrix.keys():
            listOfUniqueCharacters.append(key)
        return listOfUniqueCharacters