from util import ListNode, LinkedList, arr_to_llist 

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
    list = LinkedList()
    list.head = ListNode("Mon")
    # Create llist from array
    list = arr_to_llist([1, 2, 3, 4, 5])
    list.listprint()
    # Reverse it and test print
    rev_list = reverse_list(list.head)
    rev_list.listprint()