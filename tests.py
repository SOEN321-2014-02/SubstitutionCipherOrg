__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'
'''
File: test-digrammatrix.py
Description: Test class file to test digrammatrix class methods
Reference: https://docs.python.org/3/library/unittest.html
File version:  0.0.1
Date-created: 2014-11-01
Last-update:  2014-11-01
Python Ver: 3.4.1
IDE: PhyCharm 3.4.1
'''

#import statements
import random
import unittest
from digrammatrix import DigramMatrix
import utils


class TestDigramMatrix(unittest.TestCase):

    def setUp(self):
        self.test_matrix = DigramMatrix("Test")  # object to use for testing

    def test_learn(self):
        self.test_matrix.learn("abcdefg")
	
