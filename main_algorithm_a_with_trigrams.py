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
from trigram_space import TrigramSpace
from random import randint
from pprint import pprint
from heapq import *
import sys
import copy
import utils
import ast
import math

#initialize file_name
file_name = ""
#file_name = "ciphertext.txt"   #*Debug - filename for importing

#get filename from command line arguments
if len(sys.argv) < 3:
  print()
  print("Usage: ")
  print("  python3 main.py <ciphertext> <training_text> [actual_key]")
  print("    - <ciphertext> The location of the file containing ciphertext")
  print("    - <training_text> The location of the file containing the training text")
  print("    - [actual_key] The actual key used to encrypt the ciphertext")
  print()
  sys.exit()

file_name = sys.argv[1]
training_text_file_location = sys.argv[2]
actual_key = None

# read in the actual key
if len(sys.argv) > 3:
  with open(sys.argv[3], 'r') as actual_key_file:
    actual_key_text = actual_key_file.read()
    actual_key = ast.literal_eval(actual_key_text)


# read in ciphertext
file_to_read_object = open(file_name, 'r')
file_text = file_to_read_object.read()
file_to_read_object.close()

alphabet = "abcdefghijklmnopqrstuvwxyz "

# train english matrixes
base_matrix = TrigramSpace(alphabet)
english_monograms = MonogramMatrix()
with open(training_text_file_location, 'r', -1, 'utf-8', 'replace') as training_text:
  text = training_text.read()
  normalized_text = utils.normalize(text)
  base_matrix.learn(normalized_text)
  english_monograms.learn(normalized_text)


# generate initial guess
key = SubstitutionKey("Guess key")
english_monograms.setCharacterAsMostCommon(' ')
guess = Guess(english_monograms.getListOfUniqueCharacters())
guess.randomGuessOneCharacter()
guess_mapping = english_monograms.generateMappingBasedOnFrequencies(file_text)
guess.setGuess(guess_mapping)
key.set(guess.get())
if actual_key:
  pprint(actual_key)
  pprint(guess_mapping)
  print("score: " + str(utils.compare_keys(actual_key, guess_mapping)))

current_decryption = key.decrypt(file_text)
ciphertext_matrix = TrigramSpace(alphabet)
ciphertext_matrix.learn(current_decryption)


# compute initial difference & deep copy the key
current_bigram_difference = base_matrix.compare_to(ciphertext_matrix)
key_copy = copy.deepcopy(key)
ciphertext_matrix_copy = copy.deepcopy(ciphertext_matrix)

# initialize open list
open_list = []
depth = 0
log_depth = 0 if depth == 0 else math.log10(depth)
heappush(open_list, (current_bigram_difference + log_depth, depth, key_copy))
best = (current_bigram_difference + log_depth, depth, key_copy)

# build decreasing vector
monogram_matrix = MonogramMatrix()
monogram_matrix.learn(file_text)
decreasing_vector = monogram_matrix.get_decreasing_vector()

# start solving .. 
for i in range(0, 100):
  a = 1
  b = 1
  current_item = heappop(open_list)
  current_bigram_difference = current_item[0]
  depth = current_item[1]
  log_depth = 0 if depth == 0 else math.log10(depth)
  key = current_item[2]
  current_decryption = key.decrypt(file_text)
  ciphertext_matrix = TrigramSpace(alphabet)
  ciphertext_matrix.learn(current_decryption)

  while True:

    # pick a and b
    alpha = decreasing_vector[a]
    beta = decreasing_vector[a+b]

    # deep copy
    key_copy = copy.deepcopy(key)
    ciphertext_matrix_copy = TrigramSpace(alphabet)

    # swap rows / cols in key & matrix
    key_copy.swap(alpha, beta)
    ciphertext_matrix_copy.learn(key_copy.decrypt(file_text))

    # continue computation of step 6
    a += 1
    if (a + b) > 26:
      a = 1
      b += 1
      if b == 26:
        break

    # compute difference
    bigram_difference = base_matrix.compare_to(ciphertext_matrix_copy)
    if bigram_difference < current_bigram_difference:
      print("found a better mapping")
      print('bigram difference: ' + str(bigram_difference))
      print("depth: " + str(depth + 1))
      if actual_key:
        print('score: ' + str(utils.compare_keys(actual_key, key_copy.keyValues)))
      heappush(open_list, (bigram_difference + log_depth, depth + 1, key_copy))
      if bigram_difference < best[0]:
        best = (bigram_difference + log_depth, depth + 1, key_copy)

  print("end of iteration")
  print("current best: ")
  print("  score: " + str(utils.compare_keys(actual_key, best[2].keyValues)))
  print("  bigram difference: " + str(best[0]))
  print("  depth: " + str(best[1]))






# print current decryption
print(key.decrypt(file_text))