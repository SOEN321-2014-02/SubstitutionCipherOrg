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
# from and import statements
import numpy


class DigramMatrix:
    #define class variables


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
        if len(text) % 2 is not 0:
            text += "-"

        #get the character pairs
        counter = 0  #initialize counter
        while counter < len(text)-1:
            char01 = text[counter].lower()
            char02 = text[counter+1].lower()
            # print(char01 + ":" + char02)
            #does this pair already exist in the dictionary?
            if char01 in self.matrix and char02 in self.matrix[char01]:
                #enter pair count into dictionary
                self.matrix[char01][char02] += 1
            else:
                #create new entry
                self.matrix[char01][char02] = 1
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
        for key in sorted(self.matrix):
            value = self.matrix[key]
            print("------")
            if key[0] is " ":
                key00 = "_"
            else:
                key00 = key[0]
            if key[1] is " ":
                key01 = "_"
            else:
                key01 = key[1]
            print (key00+key01 + " | " + str(value))
        print("------")
