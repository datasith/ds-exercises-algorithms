class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        print(self.val)
# Add any helper functions you may need here


def reverse(head):
    dummy = Node(0)
    dummy.next = head

    while head:
        next = head.next
        head.next = dummy
        dummy = head
        head = next
        
    return dummy.next

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

l = reverse(a)

while l:
    print(l.val, end='->')
    l = l.next