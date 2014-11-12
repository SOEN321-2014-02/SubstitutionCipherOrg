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
if len(sys.argv) < 3:
  print()
  print("Usage: ")
  print("  python3 main.py <ciphertext> <training_text>")
  print("    - <ciphertext> The location of the file containing ciphertext")
  print("    - <training_text> The location of the file containing the training text")
  print()
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
a = 0
b = 0

# start solving .. 
for i in range(0, 10000):

  # pick a and b
  print("a:" + str(a))
  print("b:" + str(b))
  print("diff: " + str(current_bigram_difference))
  monogram_matrix = MonogramMatrix('')
  monogram_matrix.learn(key.decrypt(file_text))
  decreasing_vector = monogram_matrix.get_decreasing_vector()
  alpha = decreasing_vector[a]
  beta = decreasing_vector[a+b]

  # swap rows / cols in key & matrix
  key_copy.swap(alpha, beta)
  ciphertext_matrix_copy.swap(alpha, beta)

  # continue computation of step 6
  a += 1
  if (a + b) > 26:
    a = 0
    b += 1
    if b == 26:
      print(key.decrypt(file_text))
      sys.exit()

  # compute difference
  bigram_difference = base_matrix.compare_to(ciphertext_matrix_copy)
  if bigram_difference < current_bigram_difference:
    a = 0
    b = 0
    current_bigram_difference = bigram_difference
    print(current_bigram_difference)
    key = key_copy
    ciphertext_matrix = ciphertext_matrix_copy

  # deep copy
  key_copy = copy.deepcopy(key)
  ciphertext_matrix_copy = copy.deepcopy(ciphertext_matrix)






# print current decryption
print(key.decrypt(file_text))