import unittest
from primeno2 import prime_num
class TestPrime(unittest.TestCase):
   #Tests that our function gives correct results
   #prime_no=50 outputs [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  def test_primenumbers(self):
      self.assertEqual(primeno2.prime_num(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    
    #Tests that negative  numbers returns an error message.
  def test_negative_numbers(self):
      self.assertEqual(primeno2.prime_num(-5), 'Only positive numbers are allowed')