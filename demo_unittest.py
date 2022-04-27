import unittest

def find_max(array):
    max_val = array[0]
    for element in array:
        max_val = max(max_val, element)
    return max_val

class CustomTest(unittest.TestCase):
    def test01(self):
        array = [1,3,343,45,6,6778]
        self.assertEqual( find_max(array), max(array) )

if __name__ == '__main__':
    unittest.main()