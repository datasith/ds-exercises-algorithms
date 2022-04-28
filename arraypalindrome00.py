def is_palindrome(s: str) -> bool:

    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return True

    is_palindrome(s[1:-1])

    return False

import unittest
class CustomTest(unittest.TestCase):
    def test_01(self):
        input = "kaak"
        self.assertEqual( is_palindrome(input), True )
    def test_02(self):
        input = "qwwqqwr"
        self.assertEqual( is_palindrome(input), False )
    def test_03(self):
        input = "1234567890987654321"
        self.assertEqual( is_palindrome(input), True )    

if __name__ == '__main__':
    unittest.main()
 