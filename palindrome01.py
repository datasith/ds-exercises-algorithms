def is_palindrome(input, i, j):
    if len(input) == 0:
        return False

    if input[i] != input[j]:
        return False

    if j - i <=2:
        return True

    return is_palindrome(input, i+1, j-1)

import unittest
class CustomTest(unittest.TestCase):
  def test_01(self):
    input = "kaak"
    self.assertEqual( is_palindrome(input, 0, len(input)-1), True )
  def test_02(self):
    input = "qwwqqwr"
    self.assertEqual( is_palindrome(input, 0, len(input)-1), False )
  def test_03(self):
    input = "1234567890987654321"
    self.assertEqual( is_palindrome(input, 0, len(input)-1), True )    

if __name__ == '__main__':
  unittest.main()