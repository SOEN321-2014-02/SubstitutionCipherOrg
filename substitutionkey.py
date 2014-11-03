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
import utils


class SubstitutionKey:
    #define class variables
      # none


    def __init__(self, name):
        #define instance variables
        self.name = name  #substitution key name
        self.substitution_key = [0 for i in range(27)]  # option 1


    def update_key(self, character, value):
        return 1


    def reset_key(self):
        return 1