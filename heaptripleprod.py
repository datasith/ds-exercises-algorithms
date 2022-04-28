def findMaxProduct(arr):
    heap = arr[0:3]
    output = [-1,-1] + [ heap[0]*heap[1]*heap[2] ]
  
    for c in arr[3:]:
        heap.append(c)
        heap.sort()
        heap = heap[1:]
        output.append(heap[0]*heap[1]*heap[2])

    return output

import unittest
class CustomTest(unittest.TestCase):
    def test_01(self):
        arr = [1, 2, 3, 4, 5] 
        output = [-1, -1, 6, 24, 60]
        ans = findMaxProduct(arr)
        print(ans)
        self.assertEqual(ans, output)

if __name__ == '__main__':
    unittest.main()