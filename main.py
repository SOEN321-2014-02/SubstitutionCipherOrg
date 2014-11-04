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
import sys

#initialize file_name
file_name = ""
'file_name = "ciphertext.txt"   #*Debug - filename for importing

#get filename from command line arguments
if len(sys.argv) > 1:
    file_name = sys.argv[1]
    print(file_name)
else:
    if file_name is "":
        print("Filename required")
        exit()

#open file for reading
file_to_read_object = open(file_name, 'r')
#read text from file
file_text = file_to_read_object.read()


## algorithm steps ##
# i) Import an English language frequency matrix (26 char plus space)
#create english language digram frequency matrix
english_language_matrix = DigramMatrix("Ciphertext")

#create substitution key
#sub_key = SubstitutionKey("Key")

#send text to matrix
#english_language_matrix.learn("this is some text that I am including at")  # test with text
english_language_matrix.learn(file_text)  # use text from file

#* Debug - print matrix contents for ciphertext
#english_language_matrix.print_string()
english_language_matrix.print_table()

# ii) Create a guess key matrix called k
  # - (OPTIONAL) create the guess by:
  # - calculating the single character frequency matrix for the ciphertext
  # - comparing English single character matrix to ciphertext single character matrix
#create experimental guess key digram frequency matrix


# iii) Calculate the Digram frequency matrix for the decrypted ciphertext
#create decrypted ciphertext digram frequency matrix


# iv) Perform a matrix addition function on the ciphertext Digram frequency matrix  and the English Digram frequency matrix and assign result to v
# v =

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