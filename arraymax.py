import unittest

def selection_sort(array):
    idx = 0
    while idx < len(array):
        print('selection sort: ' + str(array))
        for i in range(idx, len(array)):
            if array[i] < array[idx]:
                array[idx], array[i] = array[i], array[idx]
        idx += 1
    return array

class CustomTest(unittest.TestCase):
    def test01(self):
        input = [4, 7, 2, 8, 10, 9]
        self.assertEqual( selection_sort(input)[-1], max(input) )

if __name__ == '__main__':
    unittest.main()