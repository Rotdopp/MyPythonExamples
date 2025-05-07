from collections import deque

#Binary Trees
class Tree_Node:
    def __init__(self, val, left=None, right =None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

A = Tree_Node(1)
B = Tree_Node(2)
C = Tree_Node(3)
D = Tree_Node(4)
E = Tree_Node(5)
F = Tree_Node(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

#          1
#      2        3
#   4     5   10




#Normally tree is in only A because it is the root of the tree and if you traverse the tree you can acssess other node's from it


print(A)
print()

#Recursive Pre Order Traversal DFS(Depth First Search) Time: O(n), Space: O(n)
def pre_order(node):
    if not node:
        return

    print(node)
    pre_order(node.left)
    pre_order(node.right)

pre_order(A)
print()

#Recursive In Order Traversal DFS(Depth First Search) Time: O(n), Space: O(n)
def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)

in_order(A)
print()


#Iterative Pre Order Traversal DFS(Depth First Search) Time: O(n), Space: O(n)

def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

pre_order_iterative(A)
print()


# Level Order Traversal BFS(Breadth First Search) Time: O(n), Space: O(n)

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

level_order(A)
print()


#Check if Value Exists (DFS) Time: O(n), Space: O(n)

def search(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)

print(search(A, 6))
print(search(A, 5))
print()

# Binary Search Trees (BSTs) (Node's left childs are smaller than the parent, Node's right childs bigger than parent)
# Time: O(log n), Space: O(log n)



def search_BST(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    if node.val > target: return search_BST(node.left, target)
    else: return search_BST(node.right, target)

print(search(A, 6))
print(search(A, 5))








