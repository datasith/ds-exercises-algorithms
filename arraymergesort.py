def mergesort(input):
    if len(input) == 1:
        return input

    pivot = len(input) // 2
    left = mergesort(input[0:pivot])
    right = mergesort(input[pivot:])

    output = merge(left, right)
    return output

def merge(left, right):
    i = j = 0
    n, m = len(left), len(right)
    output = []
    while i < n and j < m:
        if left[i] <= right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append(right[j])
            j+=1
    if i < n:
        output += left[i:]
    elif j < m:
        output += right[j:]
    return output

import unittest
class CustomTest(unittest.TestCase):
    def test01(self):
        input = [9,8,-24,1,3,2,7,5,6]
        ans = mergesort(input)
        self.assertEqual(ans, [-24, 1, 2, 3, 5, 6, 7, 8, 9], "check yo code")

if __name__ == '__main__':
    unittest.main()