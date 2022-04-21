class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(node):
    if not node:
        return
    print('pre',node.val)
    print_list(node.next)
    print('post', node.val)



if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    a.next = b
    b.next = c

    print_list(a)