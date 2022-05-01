import unittest

def selection_sort(array):
    idx = 0 
    while idx < len(array):
        print('sorting: ', array)
        for i in range(idx, len(array)):
            if array[i] < array[idx]:
                array[i], array[idx] = array[idx], array[i]
        idx += 1
    return array

class CustomTest(unittest.TestCase):
    def test01(self):
        input = [4, 7, 2, 8, 10, 9]
        output = selection_sort(input)
        print(output)
        self.assertEqual( output[-1], max(input) )

if __name__ == '__main__':
    unittest.main()