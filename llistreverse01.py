from utils import ListNode, LinkedList, arr_to_llist 

# class ListNode:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return LinkedList(head=prev)

if __name__ == '__main__':
    # Create llist from array
    llist = arr_to_llist([1, 2, 3, 4, 5])
    llist.listprint()
    # Reverse it and test print
    rev_llist = reverse_list(llist.head)
    rev_llist.listprint()