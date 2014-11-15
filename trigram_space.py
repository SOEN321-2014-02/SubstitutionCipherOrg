
import utils
import math

class TrigramSpace:

  def __init__(self, alphabet):
    self.alphabet = alphabet
    self.length = 0
    self.vector_space = {}
    for a in alphabet:
      for b in alphabet:
        for c in alphabet:
          if not a in self.vector_space:
            self.vector_space[a] = {}
          if not b in self.vector_space[a]:
            self.vector_space[a][b] = {}
          self.vector_space[a][b][c] = 0

  def learn(self, text):
    self.length += len(text)
    for i in range(0, len(text) - 3):
      a = text[i]
      b = text[i+1]
      c = text[i+2]
      self.vector_space[a][b][c] += 1

  def compare_to(self, other):
    length = len(self.alphabet) - 1
    diff = 0
    for i in range(0, length):
      a = utils.element_to_char(i)
      for j in range(0, length):
        b = utils.element_to_char(j)
        for k in range(0, length):
          c = utils.element_to_char(k)
          self_value = self.vector_space[a][b][c] / self.length
          other_value = other.vector_space[a][b][c] / other.length
          diff += math.fabs(self_value - other_value)
    return diff

  # def swap(self, alpha, beta):
  #   a = utils.char_to_element(alpha)
  #   b = utils.char_to_element(beta)
  #   length = len(self.alphabet) - 1
  #   for i in range(length):
  #     tmp = self.matrix[i][]


  #     f = utils.char_to_element(first)
  #     s = utils.char_to_element(second)
  #     for i in range(27):
  #         tmp = self.matrix[i][f]
  #         self.matrix[i][f] = self.matrix[i][s]
  #         self.matrix[i][s] = tmp
  #     for i in range(27):
  #         tmp = self.matrix[f][i]
  #         self.matrix[f][i] = self.matrix[s][i]
  #           self.matrix[s][i] = tmp
