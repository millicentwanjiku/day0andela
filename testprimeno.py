import unittest

import primeno

class TestPrime(unittest.TestCase):
   #Tests that our function gives correct results
   #prime_no=50 outputs [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
	def test_primenumbers(self):
		self.assertEqual(primeno.prime_num(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
	#Test that if you input 2 if output 2
	def test_generate_output_two_only(self):
		self.assertEqual(primeno.prime_num(2),[2])
    
    #Tests that negative  numbers returns an error message.
	def test_negative_numbers(self):
		self.assertEqual(primeno.prime_num(-5), 'Only positive numbers are allowed')
     #Tests that the inputs are integers
	def test_number_is_int(self):
		self.assertEqual(primeno.prime_num('str'), 'Only intergers are accepted')
	#Test that the input is a list
	def test_number_is_list(self):
		self.assertEqual(primeno.prime_num([]), 'List not allowed')
	#Test that the input is a dictionary
	def test_number_is_dictionary(self):
		self.assertEqual(primeno.prime_num({}), 'Dictionary not allowed')
	#Test if tuple is allowed
	def test_number_is_tuple(self):
		self.assertEqual(primeno.prime_num(()), 'Tuple not allowed')

	def test_number_is_dictionary(self):
		self.assertEqual(primeno.prime_num([()]), 'Dictionary not allowed')

     #Tests if the input is one which is not a prime number
	def test_number_one(self):
		self.assertEqual(primeno.prime_num(1),'one is not a prime number')
	#Test if it returns list
	def test_return_list(self):
		self.assertIsInstance(primeno.primenum(50), list)
	#Test if it returns correct length
	def test_return_list_length(self):
		self.assertEqual(len(generate_prime(3)), 2)
	


