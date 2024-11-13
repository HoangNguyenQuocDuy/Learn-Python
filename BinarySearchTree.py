from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def addNode(root, val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = addNode(root.left, val)
    else:
        root.right = addNode(root.right, val)

    return root


aList = [10, 20, -10, 40, 15, 8, 6, -15]

root = Node(aList[0])
for idx in range(1, len(aList)):
    root = addNode(root, aList[idx])


#DFS
def inOrder(root):
    if root is None:
        return
    print(root.val)
    inOrder(root.left)
    inOrder(root.right)


def preOrder(root):
    if root is None:
        return
    preOrder(root.left)
    print(root.val)
    preOrder(root.right)


def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val) 
    

#BFS
def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        currentNode = queue.popleft()
        print(currentNode.val, end=" ")
        
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)


# print('IN ORDER: ', inOrder(root))
# print('PRE ORDER: ', preOrder(root))
# print('POST ORDER: ', postOrder(root))
# print('BFS: ', bfs(root))


def findNode(root, val):
    if root is None:
        return None    
    if val == root.val:
        return root
    elif val > root.val:
        return findNode(root.right, val)
    else:
        return findNode(root.left, val)


