__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'
'''
File: utils.py
Description: Utilities class file for Substitution Cipher
File version:  0.0.1
Date-created: 2014-11-01
Last-update:  2014-11-01
Python Ver: 3.4.1
IDE: PhyCharm 3.4.1
'''

#import statements


def char_to_ascii(char):
    #convert alpha-numeric character to ascii code (32 to space)
    ascii = 0
    ascii = ord(char)
    return ascii

def ascii_to_char(ascii):
    #convert ascii code to alpha-numeric character (32 to space)
    char = ''
    char = chr(ascii)
    return char

def char_to_element(char):
    #convert alpha-numeric character to array element
    ascii = char_to_ascii(char)  #get ascii code for char
    element = (ascii - 64) % 32
    return element

def ascii_to_element(ascii):
    #convert ascii code to array element location(space to 0)
    element = (ascii - 64) % 32
    return element

def element_to_char(element):
    #convert element number to alpha-numeric character
    if element is 0:
        return ' '
    else:
        ascii = element + 96
        return ascii_to_char(ascii)

def element_to_ascii(element):
    #convert element number to ascii code
    if element is 0:
        return 32
    else:
        return element + 96