import unittest


def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list) <= 1:
         raise Exception
         return
    forward_list = [0] * len(int_list)
    forward_list[0] = int_list[0]
    for i in range(1, len(int_list)):
        forward_list[i] = forward_list[ i - 1] * int_list[i]
    out = [1]
    for j in range(1, len(int_list)):
        out.append(forward_list[j-1])
    
    forward_list[-1] = int_list[-1]
    for i in range(len(int_list) - 2, -1, -1):
        forward_list[i] = forward_list[i + 1] * int_list[i]
    
    for j in range(len(int_list) - 1):
        out[j] *= forward_list[j + 1]

    return out


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)