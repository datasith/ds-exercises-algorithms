from utils import LinkedList, ListNode

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def llist_find(head, target):
    if head is None:
        return False

    if head.val == target:
        return True

    return llist_find(head.next, target)

import unittest

class CustomTest(unittest.TestCase):
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    llist = LinkedList(head=a)
    llist.listprint()    
    def test01(self):
        ans = llist_find(self.a, 4)
        self.assertEqual(ans, False)
    
    def test02(self):
        ans = llist_find(self.a, 3)
        self.assertEqual(ans, True)

if __name__ == '__main__':
    unittest.main()

