__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'
'''
File: digrammatrix.py
Description: Matrix class file to generate digram matrices for decrypting substitution ciphers
File version:  0.0.1
Date-created: 2014-10-18
Last-update:  2014-10-18
Python Ver: 3.4.1
IDE: PhyCharm 3.4.1
'''

#import statements
import numpy
import utils


class DigramMatrix:
    #define class variables
      # none

    def __init__(self, name):
        #define instance variables
        self.name = name  #matrix name
        self.matrix = [[0]*27 for i in range(27)]  # option 1

        '''
        # Alternative ways of initializing the matrix with sets
        ### Dictionary method
        # self.matrix = {}  #matrix initialize
        # self.matrix[0,1] = 5  # add data to dictionary
        # self.matrix[116, 104] += 1
        # print(self.matrix[116, 104])  # print data from dictionary

        ### Set method
        self.matrix = [[0]*27 for i in range(27)]  # option 1
        self.matrix = numpy.zeros((27,27))         # option 2 with numpy module imported
        self.matrix[0][5] = 15
        print(self.matrix[0][5])
        '''

    def get_name(self):
        #return the name of this matrix
        return self.name

    def learn(self, text):
        #build the matrix given body of text
        print("Learning")
        #is text length odd? add extra padding character
        #if len(text) % 2 is not 0:
        #    text += "-"

        #get the character pairs
        counter = 0  #initialize counter
        while counter < len(text)-1:
            char01 = text[counter].lower()
            char02 = text[counter+1].lower()
            # print(char01 + ":" + char02)

            #increment the counter for this pair
            self.matrix[utils.char_to_element(char01)][utils.char_to_element(char02)] += 1

            #increment the while loop counter
            counter += 1

    def swap_rows(self, row01, row02):
        #swap two rows
        print("Swapping Rows")

    def swap_cols(self, col01, col02):
        #swap two columns
        print("Swapping Columns")

    def compare_to(self, digrammatrix):
        #compare this matrix to another one
        print("Comparing")

    def print_string(self):
        for key01 in range(len(self.matrix)):
            for key02 in range(len(self.matrix)):
                value = self.matrix[key01][key02]
                print("-------")
                print (utils.element_to_char(key01) + "," + utils.element_to_char(key02) + " | " + str(value))
            print("-------")
