import unittest

def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    if len(list_of_ints) < 3:
        raise Exception
        return
    
    # window = [list_of_ints[0], list_of_ints[1], list_of_ints[2]]
    # min_number = min(window)
    # min_index = window.index(min_number)
    # prod = reduce(lambda x, y: x*y, window)
    # for i in range(3, len(list_of_ints)):
    #     if list_of_ints[i] > min_number:
    #         window[min_index] = list_of_ints[i]
    #         min_number = min(window)
    #         min_index = window.index(min_number)
    #         prod = reduce(lambda x, y: x*y, window)
    # return prod
    
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    hp3 = -99999999999
    hp2 = list_of_ints[0] * list_of_ints[1]
    lp2 = list_of_ints[0] * list_of_ints[1]
    for i in range(2, len(list_of_ints)):
        hp3 = max(hp3, list_of_ints[i] * hp2, list_of_ints[i] * lp2)
        hp2 = max(hp2, list_of_ints[i] * highest, list_of_ints[i] * lowest)
        lp2 = min(lp2, list_of_ints[i] * highest, list_of_ints[i] * lowest)
        highest = max(highest, list_of_ints[i])
        lowest = max(lowest, list_of_ints[i])
    return hp3

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