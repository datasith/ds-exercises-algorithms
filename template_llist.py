import unittest
from utils import ListNode, LinkedList, arr_to_llist

# class ListNode:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None
#
# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

def my_function(root, arg=None):
    return []

class CustomTest(unittest.TestCase):
    a = ListNode("a")
    b = ListNode("b")
    c = ListNode("c")
    d = ListNode("d")
    e = ListNode("e")
    f = ListNode("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    llist = LinkedList(a)
    # Create llist from array
    # list = arr_to_llist([1, 2, 3, 4, 5])
    def test01(self):
        input = []
        self.llist.listprint()
        self.assertEqual( my_function(self.a, 'e'), input )

if __name__ == '__main__':
    unittest.main()