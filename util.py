class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.val, end=" -> ")
            printval = printval.next
        print("None")

def arr_to_llist(arr):
    list = LinkedList(ListNode(arr[0]))
    tail = list.head
    for e in arr[1:]:
        node = ListNode(e)
        tail.next = node
        tail= tail.next
    return list

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

if __name__ == '__main__':
    # see the demo scripts
    # demo_llist.py
    # demo_tree.py
    pass