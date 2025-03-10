import os
import time

from collections import deque

#Stacks
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
element = stack.pop()      # Pop (removes 3)
print(stack)
print(element)
print(stack[-1])
print("-----------------")

#Queues
queue = deque()
queue.append(0)
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
element2 = queue.popleft()  # Dequeue (removes 0)
print(queue)
print(element2)
print(queue[0])


for i in range(2):
    print(f"Count: {i}")
    time.sleep(1)  # Wait for 1 second
print("LinkedLists")
time.sleep(1)


#LinkedLists
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

#Traverse the list - O(n)

curr = Head

while curr:
    print(curr)
    curr = curr.next


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))


display(Head)

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False


print(search(Head, 2))
print(search(Head, 9))
print(search(Head, 7))

print(input("You want to continue ? "))


#Doubly Linked Lists
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1)
print(head)
print(tail)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('<->'.join(elements))

display(head)

def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)

display(head)

def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)

display(head)
print(tail.next)