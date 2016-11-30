import unittest

import primeno

class TestPrime(unittest.TestCase):
   #Tests that our function gives correct results
   #prime_no=50 outputs [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
	def test_primenumbers(self):
		self.assertEqual(primeno.prime_num(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
	#Test that the function accepts only integers
	def test_number_is_an_integer(self):
		self.assertEqual(primeno.prime_num('str'), 'only intergers are allowed')
	 #Tests if the input is one it returns an empty list
	def test_number_one(self):
		self.assertEqual(primeno.prime_num(1),[])
	 #Tests if the input is two it returns only two in the list
	def test_number_two(self):
	 	self.assertEqual(primeno.prime_num(2),[2])
	 #Tests if the input is negative and it returns an error
	def test_number_is_an_integer(self):
		self.assertEqual(primeno.prime_num(-5), 'Negative numbers not allowed')
	#Tests if a number does not return empty list given a number
	def test_number_does_not_return_an_empty_list(self):
		self.assertEqual(primeno.prime_num(5), [2,3,5])
	#Tests if number does not accept list inputs
	def test_number_input_is_list(self):
		self.assertEqual(primeno.prime_num([]), 'only intergers are allowed')
	#Tests if number does not accept dictionaries
	def test_number_input_is_dictionary(self):
		self.assertEqual(primeno.prime_num({}), 'only intergers are allowed')
	#Tests if the length input is per expected
	def test_return_list_length(self):
		self.assertEqual(len(primeno.prime_num(3)), 2)
	def test_return_zero(self):
		self.assertEqual(primeno.prime_num(0),[])
	def test_number_input_is_float(self):
		self.assertEqual(primeno.prime_num(58.3694), 'only intergers are allowed')

	
    
    
