class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root == None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


def delete(root, data):
    if root == None:
        return
    else:
        if data < root.data:
            root.left = delete(root.left, data)
        elif data > root.data:
            root.right = delete(root.right, data)
        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            else:
                replace = find(root.right)
                root.data = replace.data
                root.right = delete(root.right, replace.data)
        return root


def find(root):
    temp = root
    while(temp.left != None):
        temp = temp.left
    return temp

def traverse(root):
    if root == None:
        return
    traverse(root.left)
    print(root.data, " ")
    traverse(root.right)


root = None
root = insert(root, 8)
root = insert(root, 5)
root = insert(root, 12)
root = insert(root, 1)
root = insert(root, 10)
root = insert(root, 6)
root = insert(root, 4)
traverse(root)
root = delete(root, 5)
traverse(root)
