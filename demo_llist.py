from util import ListNode, LinkedList, arr_to_llist 

# class ListNode:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

if __name__ == '__main__':
    list = LinkedList()
    list.head = ListNode("Mon")
    # Create llist from array
    list = arr_to_llist([1, 2, 3, 4, 5])
    list.listprint()