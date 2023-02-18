class BSTNode:
  def __init__(self, key, value=None):
    self.key = key
    self.value = value
    self.right = None
    self.left = None
    self.parent = None
  
"""Question: Write a function to insert a new node into a BST

We use the BST-property to perform insertion efficiently:

1. Starting from the root node, we compute the key to be inserted with the current
node's key
2. If the key is the smaller, we recursively insert it in the left subtree (if it exists)
or attach it as the left child if no left subtree exists.
3. If the key is larger, we recursively inset it in the right subtree (if it exist) or 
attach it as the right child if o subtree exists.
"""

def insert(node, key, value): 
  if node is None:
    node = BSTNode(key, value)
  elif key < node.key:
    node.left = insert(node.left, key, value)
    node.left.parent = node
  else:
    node.right = insert(node.right, key, value)
    node.right.parent = node
  return node


"""Question: Find the value associated with a given key in a BST"""

def find(node, key):
  if node is None:
    return None
  if key == node.key:
    return node
  if key < node.key:
    return find(node.left, key)
  if key > node.key:
    return find(node.right, key)
  
"""Question: write a function to update the value associated with a given key 
within a BST"""

def update(node, key, value):
  target = find(node, key)
  if target is not None:
    target.value = value


"""Question: Write a function to retrieve all the key-value pairs stored in a 
BST in the stored order of keys"""

def list_all(node):
  if node is None:
    return []
  return (list_all(node.left) + 
          [(node.key, node.value)] + 
          list_all(node.right))

"""Determine the time complexity and space complexity of list_all"""

"""Question: Write a function to determine if a binary tree is balanced

Here's a recursive strategy:

1.Ensure that the left subtree is balanced
2. Ensure that the right subtree is balanced
3. Ensure that the difference between heights of left subtree and right subtree is nor more than 1"""

def is_balanced(node):
  if node is None:
    return True, 0
  balanced_left, height_left = is_balanced(node.left)
  balanced_right, height_right = is_balanced(node.right)
  balanced = balanced_left and balanced_right and abs(height_left - height_right) <= 1
  height = 1 + max(height_left, height_right)
  return balanced, height


"""Question: Write a function to create a balanced BST from a sorted list/array
of key-value pairs.

We can use a recursive strategy here, turning the middle element of the list into 
the root, and recursively creating left and right subtree.
"""

def make_balanced_bst(data, lo=0, hi=None, parent=None):
  if hi is None:
    hi = len(data) - 1
  if lo > hi:
    return None
  
  mid = (lo + hi) // 2
  key, value = data[mid]

  root = BSTNode(key, value)
  root.parent = parent
  root.left = make_balanced_bst(data, lo, mid-1, root)
  root.right = make_balanced_bst(data, mid+1, hi, root)

  return root

"""Question: Write a function to balance an unbalanced binary search tree.

We first perform an in-order traversal, then create a balanced BST using function
defined earlier.
"""

def balanced_bst(node):
  return make_balanced_bst(list_all(node))


"""After every insertion,we can balance the tree. This way the tree will
remain balanced

Complexity of the various operations in a balanced BST

- insert - O(log N) + O(N) = O(N)
- find - O(log N)
- update - O(log N)
- list all - O(N)
"""
## Helper functions
def tree_size(node):
  if node is None:
    return 0
  return 1 + tree_size(node.left) + tree_size(node.right)

def display_keys(node, space="\t", level=0):
  if node is None:
    print(space*level + " ")
    return
  
  if node.left is None and node.right is None:
    print(space*level + str(node.key))
    return
  
  # If the node has children
  display_keys(node.right, space, level + 1)
  print(space*level + str(node.key))
  display_keys(node.left, space, level + 1)


# Bringing everything together
class TreeMap():
  def __init__(self) -> None:
    self.root = None
  
  def __setitem__(self, key, value):
    node = find(self.root, key)
    if not node:
      self.root = insert(self.root, key, value)
      self.root = balanced_bst(self.root)
    else:
      update(self.root, key, value)
  
  def __getitem__(self, key):
    node = find(self.root, key)
    return node.value if node else None
  
  def __iter__(self):
    return (x for x in list_all(self.root))
  
  def __len__(self):
    return tree_size(self.root)

  def display(self):
    return display_keys(self.root) 