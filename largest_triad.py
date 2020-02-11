import unittest


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers

    # check list length: if less than 3, throw exception 
    # three-number list return product of all
    if len(list_of_ints) < 3:
      raise Exception('too few numbers in list')
    elif len(list_of_ints) is 3:
      return list_of_ints[0]*list_of_ints[1]*list_of_ints[2]
    
    # create list of lists for combinations of two values
    prods_of_two = {}
    for i in range(0, len(list_of_ints)):
      prods_of_two[i] = {}
      for j in range(0, i):
        if i is not j:
          prods_of_two[i][j] = list_of_ints[i]*list_of_ints[j]
    
    # find max possible triad for each value in list_of_ints
    current_max = float('-inf')
    for k in range(0, len(list_of_ints)):
      # loop through prods_of_two
      for i in range(0, len(list_of_ints)):
        for j in range(0, i):
          if i is not j and i is not k and j is not k:
            prod_of_three = prods_of_two[i][j]*list_of_ints[k]
            if prod_of_three > current_max:
              current_max = prod_of_three          

    return current_max


















# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)