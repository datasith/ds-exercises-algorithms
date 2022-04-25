# example: b1 = "1111", b2 = "1"
def ba(b1, b2):
  hashmap = {
      ('1','0') : ('1', '0'),
      ('0','1') : ('1', '0'),
      ('0','0') : ('0', '0'),
      ('1','1') : ('1', '1')
  }
  
  

import unittest
class TestStringMethods(unittest.TestCase):
  def test_1(self):
    self.assertEqual(ba("1", "0"), "1")
  
  def test_2(self):
    self.assertEqual(ba("1", "1"), "10")
  
  def test_3(self):
    self.assertEqual(ba("10", "1"), "11")

  def test_4(self):
    self.assertEqual(ba("10", "10"), "100")

  def test_5(self):
    self.assertEqual(ba("111", "1"), "1000")

  def test_6(self):
    self.assertEqual(ba("1", "111"), "1000")

  def test_7(self):
    self.assertEqual(ba("10101", "101"), "11010")

if __name__ == '__main__':
  unittest.main()