__author__ = 'SOEN321-2014-02 Group: Connor Bode, Sid the Banzai Master, Eric Bozikian, Norman Mirotchnick'
'''
File: test-digrammatrix.py
Description: Test class file to test digrammatrix class methods
References:
  - https://docs.python.org/3/library/unittest.html
  - http://pythontesting.net/framework/unittest/unittest-introduction/
Run as: python test.py -v
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
from substitutionkey import SubstitutionKey
import utils


class TestDigramMatrix(unittest.TestCase):

    def setUp(self):
        self.test_matrix = DigramMatrix("Test")  # object to use for testing

    def test_learn(self):
        m = self.test_matrix
        m.learn("abab")
        self.assertEqual(m.get("a", "b"), 2)
        self.assertEqual(m.get("b", "a"), 1)

    def test_compare_to(self):
        m = self.test_matrix
        m.learn("abab")
        m2 = DigramMatrix("bla")
        m2.learn("abaa")
        self.assertEqual(m.compare_to(m2), 2)

    def test_swap(self):
        m = self.test_matrix
        m.learn("abab")
        m.swap("a", "b")
        self.assertEqual(m.get("a", "b"), 1)
        self.assertEqual(m.get("b", "a"), 2)
        
    def test_swap_2(self):
        m = self.test_matrix
        m.learn("abbcccdddd")
        self.assertEqual(m.get("b", "c"), 1)
        m.swap("a", "d")
        self.assertEqual(m.get("a", "a"), 3)
        self.assertEqual(m.get("b", "b"), 1)
        self.assertEqual(m.get("c", "a"), 1)
        self.assertEqual(m.get("c", "c"), 2)
        m.swap("c", "d")
        self.assertEqual(m.get("a", "a"), 3)
        self.assertEqual(m.get("d", "a"), 1)
        self.assertEqual(m.get("d", "d"), 2)
        self.assertEqual(m.get("b", "d"), 1)
        


class TestUtils(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(utils.normalize("S.L.O.,"), "slo")
        self.assertEqual(utils.normalize("isâ€”that"), "isthat")


class TestSubstitutionKey(unittest.TestCase):

    def setUp(self):
        self.test_key = SubstitutionKey("Test")

    def test_decrypt(self):
        key = self.test_key
        self.assertEqual(key.decrypt("test"), "test")
        self.assertEqual(key.decrypt("TEst"), "test")  # test for decrypting uppercase strings

    def test_swap(self):
        key = self.test_key
        key.swap('s', 'b')
        self.assertEqual(key.decrypt("test"), "tebt")

    def test_swap2(self):
        key = self.test_key
        key.swap("t", "a")
        self.assertEqual(key.decrypt("test"), "aesa")
        key.swap("t", "e")
        self.assertEqual(key.decrypt("test"), "ease")

    def test_swap3(self):
        key = self.test_key
        first = key.keyValues['a']
        second = key.keyValues['b']
        key.swap('a', 'b')
        self.assertEqual(first, key.keyValues['b'])
        self.assertEqual(second, key.keyValues['a'])




''' ----------- RUN UNIT TESTS --------------- '''
def main():
    unittest.main()

if __name__ == '__main__':
    main()