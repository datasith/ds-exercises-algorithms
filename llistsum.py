from utils import ListNode, LinkedList, arr_to_llist 

# class ListNode:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None
#
# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

def sum_list(head):
    total = 0
    while head is not None:
        total += head.val
        head = head.next
    return total

import unittest
class CustomTest(unittest.TestCase):
    # Create llist from array
    llist = arr_to_llist([1, 2, 3, 4, 5])    
    def test01(self):
        self.llist.listprint()
        self.assertEqual( self.llist.head.val, 1 )

    def test02(self):
        self.assertEqual( sum_list(self.llist.head), 15 )

if __name__ == '__main__':
    unittest.main()