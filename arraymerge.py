import unittest

def merge(arr1, arr2):
    i = j = 0
    n, m = len(arr1), len(arr2)
    output = []

    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            output.append(arr1[i])
            i+=1
        else:
            output.append(arr2[j])
            j+=1            

    if i < n:
        output += arr1[i:]
    elif j < m:
        output += arr2[j:]

    return output

class CustomTest(unittest.TestCase):
    arr1 = [0,1,3,9]
    arr2 = [2,4,6,8,10]    
    def test01(self):
        ans = merge(self.arr1, self.arr2)
        self.assertEqual(ans, [0, 1, 2, 3, 4, 6, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()