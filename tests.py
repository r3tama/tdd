import unittest
from function import mostRepetitiveInteger

EMPTY_TESTING_LIST = []
CORRECT_TESTING_LIST = [1,2,3,4,4,4,2,4,1,1,5]

class TestFunctionUsecases(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mostRepetitiveInteger(EMPTY_TESTING_LIST)





if __name__ == '__main__':
    unittest.main()