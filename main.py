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
for i in range(0, 10000):

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
  if bigram_difference < current_bigram_difference:
    current_bigram_difference = bigram_difference
    print(current_bigram_difference)
    key = key_copy
    ciphertext_matrix = ciphertext_matrix_copy

  # deep copy
  key_copy = copy.deepcopy(key)
  ciphertext_matrix_copy = copy.deepcopy(ciphertext_matrix)




# print current decryption
print(key.decrypt(file_text))