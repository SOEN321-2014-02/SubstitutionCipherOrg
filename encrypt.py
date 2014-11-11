import sys
from pprint import pprint
from substitutionkey import SubstitutionKey
from guess import Guess

# check proper args were supplied
if(len(sys.argv) < 4):
  print("")
  print("Usage:")
  print("  python3 encrypt.py <plaintext> <key> <ciphertext>")
  print("    - <plaintext> The location of the plaintext file to read from")
  print("    - <key> The location to write the key to")
  print("    - <ciphertext> The location to write the ciphertext to")
  sys.exit("")

# collect output / input file locations
plaintext_filename = sys.argv[1]
key_filename = sys.argv[2]
ciphertext_filename = sys.argv[3]

# generate a random key
unique_characters = list("abcdefghijklmnopqrstuvwxyz ")
guess = Guess(unique_characters)
guess.randomGuessAllCharacters()
guess_dictionary = guess.get()
key = SubstitutionKey('')
key.set(guess_dictionary)

# save the key to file
with open(key_filename, 'wt') as out:
  pprint(guess_dictionary, stream=out)

# encrypt plaintext
plaintext_file = open(plaintext_filename, 'r')
plaintext = plaintext_file.read()
plaintext_file.close()
ciphertext = key.encrypt(plaintext)

# write ciphertext to file
with open(ciphertext_filename, 'w') as out:
  out.write(ciphertext)