class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        
        if current.value > new_val:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
        else:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)


    def search(self, find_val):
        return self.search_helper(self.root, find_val)
            
    def search_helper(self, node, find_val):
        
        if node:
            if node.value == find_val:
                return True
            elif node.value > find_val:
                self.search_helper(node.left, find_val)
            else:
                self.search_helper(node.right, find_val)

        return False
                
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)





""" WITH TREE ROOT NOT INITIALIZED WITH A VALUE"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root=None): # root=None To allow the instantiation of the tree without having to add a root node
        self.root = Node(root)
        
    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        # if tree is empty
        if not self.root.value:
            self.root = Node(new_val)
            return
        
        if current.value > new_val:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
        else:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)


    def search(self, find_val):
        return self.search_helper(self.root, find_val)
            
    def search_helper(self, node, find_val):
        
        if node:
            if node.value == find_val:
                print(node.value)
                return True
            elif node.value > find_val:
                self.search_helper(node.left, find_val)
            else:
                self.search_helper(node.right, find_val)

        return False
                
        
    
# Set up tree
tree = BST()

# Insert elements
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
