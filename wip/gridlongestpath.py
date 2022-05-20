from utils import print_hashmap

matrix = [
    ['T','T','.'],
    ['T','T','.'],
    ['.','T','.'],
    ['.','T','T'],
]

m, n = len(matrix), len(matrix[0])

# import unittest
# class CustomTest(unittest.TestCase):
#     def test01(self):
#         matrix = [
#             ['T','T','.'],
#             ['T','T','.'],
#             ['.','T','.'],
#             ['.','T','T'],
#         ]
#         ans = longestDownhillPath(matrix)
#         self.assertEqual(ans, 4, "check your code!")

#     def test02(self):
#         matrix = [
#             ['.','T','.'],
#             ['.','T','.'],
#             ['.','T','.'],
#             ['.','T','T'],
#             ['.','T','T'],
#             ['.','T','T'],
#         ]
#         ans = longestDownhillPath(matrix)
#         self.assertEqual(ans, 6, "check your code!")
# if __name__ == '__main__':
#     unittest.main()
