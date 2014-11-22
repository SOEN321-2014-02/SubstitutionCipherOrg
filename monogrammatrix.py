__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'

from pprint import pprint 

class MonogramMatrix:
    #Arguments:
    #	filenameToBuildFrequencyMatrix is a string representing the filename to use for building the matrix
    def __init__(self):
        self.matrix = {}
        self.uniqueCharactersInFrequencyMatrix = 0
        self.sumOfFrequencies = 0

    def learn_from_file(self, line):
        # with open(filenameToBuildFrequencyMatrix,'r') as languageFileToBuildFrequencyMatrix:
        #     #read the file by breaking it down by line
        #     for line in languageFileToBuildFrequencyMatrix:
                #now break the line down into individual characters
                for character in line:
                    #ignore new lines because we do not care about them
                    if character != '\n':
                        #treat upper and lower case characters as the same
                        if character >= 'A' and character <= 'Z':
                            character = character.lower()
                        self.sumOfFrequencies += 1
                        if character in self.matrix:
                            self.matrix[character] += 1
                        else:
                            self.matrix[character] = 1
                            self.uniqueCharactersInFrequencyMatrix += 1
                print("done")

    def generateMappingBasedOnFrequencies(self, filenameOfCipherText):
        generatedMapping = {}
        cipherMonogram = MonogramMatrix()
        cipherMonogram.learn_from_file(filenameOfCipherText)

        matrixListSorted = sorted(self.matrix, key=self.matrix.get, reverse=True)
        cipherListSorted = sorted(cipherMonogram.get(), key=cipherMonogram.get().get, reverse=True)

        if len(matrixListSorted) > len(cipherListSorted):
            endValueForLoop = len(cipherListSorted)
        else:
            endValueForLoop = len(matrixListSorted)

        for i in range(0, endValueForLoop):
            generatedMapping[cipherListSorted[i]] = matrixListSorted[i]

        required = list("abcdefghijklmnopqrstuvwxyz ")
        accounted_keys = generatedMapping.keys()
        missing_keys = list(set(required) - set(accounted_keys))
        accounted_values = [v for k, v in generatedMapping.items()]
        missing_values = list(set(required) - set(accounted_values))

        for i, v in enumerate(missing_keys):
          generatedMapping[v] = missing_values[i]

        return generatedMapping

    def learn(self, text):
        chars = list("abcdefghijklmnopqrstuvwxyz ")
        for c in chars:
          self.matrix[c] = 0
        for character in text:
          self.matrix[character] += 1

    def get_decreasing_vector(self):
        x = sorted(self.matrix, key=self.matrix.get)
        x.reverse()
        return x

    def setCharacterAsMostCommon(self, characterToMakeMostCommon):
        if characterToMakeMostCommon >= 'A' and characterToMakeMostCommon <= 'Z':
            characterToMakeMostCommon = characterToMakeMostCommon.lower()
        #Finds the highest value in the dictionary, multiplies it by 2 and then sets the given character to this value
        self.matrix[characterToMakeMostCommon] = 2*self.matrix[max(self.matrix, key=self.matrix.get)]

    #Returns the frequencies of characters in the filenameToBuildFrequencyMatrix passed as the constructor argument
    def get(self):
        return self.matrix

    def getNumberOfUniqueCharacters(self):
        return self.uniqueCharactersInFrequencyMatrix

    def getListOfUniqueCharacters(self):
        listOfUniqueCharacters = []
        for key in self.matrix.keys():
            listOfUniqueCharacters.append(key)
        return sorted(listOfUniqueCharacters)

    def getSumOfFrequencies(self):
        return self.sumOfFrequencies
