class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

def list_to_llist(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return ListNode(arr[0])
    else:
        return ListNode(arr[0], next=list_to_llist(arr[1:]))

if __name__ == '__main__':
    def reverseList(head: ListNode) -> ListNode:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node

        return prev


    # test cases
    # ListNode(val=1, next={ListNode(val=2, next={ListNode(val=3, next={ListNode(val=4, next={ListNode(val=5, next={None})})})})})    
    t1 = list_to_llist([1, 2, 3, 4, 5]) 
    # ListNode(val=1, next={ListNode(val=2, next={None})})
    t2 = list_to_llist([1, 2])  
    t3 = list_to_llist([])

    # answers
    print(reverseList(t1))
    print(reverseList(t2))
    print(reverseList(t3))    