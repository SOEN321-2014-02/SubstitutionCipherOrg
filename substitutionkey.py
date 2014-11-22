__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'
'''
File: substitution-key.py
Description: Substitution key class file to contain the substitution key table
File version:  0.0.1
Date-created: 2014-11-03
Last-update:  2014-11-03
Python Ver: 3.4.1
IDE: PhyCharm 3.4.1
'''

#import statements
from guess import Guess
from monogrammatrix import MonogramMatrix
import utils


class SubstitutionKey:
    #define class variables
      # none


    def __init__(self, name):
        #define instance variables
        self.name = name  #substitution key name
        self.keyValues = {"a":"a", "b":"b", "c":"c" , "d":"d", "e":"e", "f":"f", "g":"g", "h":"h", "i":"i", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n", "o":"o", "p":"p", "q":"q", "r":"r", "s":"s", "t":"t", "u":"u", "v":"v", "w":"w", "x":"x", "y":"y", "z":"z", " ":" "}

    def __lt__ (self, other):
      return True

    def set(self, key):
        self.keyValues = key

    def create_guess(self, file_name):
        mono_matrix = MonogramMatrix(file_name)
        guess_init = Guess(mono_matrix.getListOfUniqueCharacters())
        guess_init.randomGuessOneCharacter()
        return guess_init.get()

    def decrypt(self, oldString):
        lowerCaseString = oldString.lower()
        newString = ""
        for c in lowerCaseString:
            newString += self.keyValues[c]
        return newString

    def encrypt(self, s):
        s = s.lower()
        inverse_key = {v: k for k, v in self.keyValues.items()}
        new_string = ""
        for c in s:
            new_string += inverse_key[c]
        return new_string

    def swap(self, character, value):
        tempValue = self.keyValues[character]
        self.keyValues[character] = self.keyValues[value]
        self.keyValues[value] = tempValue

    def reset_key(self):
        return 1