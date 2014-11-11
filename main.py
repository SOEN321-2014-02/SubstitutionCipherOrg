__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'
'''
File: main.py
Description: Main file for substitution cipher decryption project
File version:  0.0.1
Date-created: 2014-09-28
Last-update:  2014-09-28
Python Ver: 3.4.1
IDE: PhyCharm 3.4.1
'''

#import statements
from digrammatrix import DigramMatrix
from substitutionkey import SubstitutionKey
from guess import Guess
from monogrammatrix import MonogramMatrix
from random import randint
import sys
import copy
import utils

#initialize file_name
file_name = ""
#file_name = "ciphertext.txt"   #*Debug - filename for importing

#get filename from command line arguments
if len(sys.argv) < 1:
  print("Usage: ")
  print("  python3 main.py <ciphertext> <training_text>")
  print("    - <ciphertext> The location of the file containing ciphertext")
  print("    - <training_text> The location of the file containing the training text")
  sys.exit()

file_name = sys.argv[1]
training_text_file_location = sys.argv[2]


# read in ciphertext
file_to_read_object = open(file_name, 'r')
file_text = file_to_read_object.read()
file_to_read_object.close()


# train english digram matrix
base_matrix = DigramMatrix("English")
with open(training_text_file_location, 'r') as training_text:
  text = training_text.read()
  normalized_text = utils.normalize(text)
  base_matrix.learn(normalized_text)


# generate initial guess
key = SubstitutionKey("Guess key")
current_decryption = key.decrypt(file_text)
ciphertext_matrix = DigramMatrix("Ciphertext")
ciphertext_matrix.learn(current_decryption)


# compute initial difference & deep copy the key
current_bigram_difference = base_matrix.compare_to(ciphertext_matrix)
key_copy = copy.deepcopy(key)
ciphertext_matrix_copy = copy.deepcopy(ciphertext_matrix)


# start solving .. 
for i in range(0, 1000):

  # pick a random a and b
  alpha_seed = randint(0, 26)
  beta_seed = randint(0, 26)
  alpha = utils.element_to_char(alpha_seed)
  beta = utils.element_to_char(beta_seed)

  # swap rows / cols in key & matrix
  key_copy.swap(alpha, beta)
  ciphertext_matrix_copy.swap(alpha, beta)

  # compute difference
  bigram_difference = base_matrix.compare_to(ciphertext_matrix_copy)
  print(bigram_difference)


# v) take the guess key k and copy it to a second variable called k'


# vi) take the ciphertext Digram frequency matrix called D and copy it to a new variable called D'

# vii) Use the swapping algorithm to swap two element in the guess key k'

# viii) swap rows and columns in D' (it says corresponding but I'm not clear on what we are corresponding with?)

# ix)  Perform a matrix addition function on the D' ciphertext Digram frequency matrix and the English Digram frequency matrix and assign result to v'

# x) Compare v' and v' and go back to step v) if v' is greater or equal to v, if v' is less than v continue to step xi)

# xi) assigned v' to v

# xii) assign k' to k

# xiii) assign D' to D

# xiv) go back to step vii) and perform the swap again


#close open file(s)
file_to_read_object.close()