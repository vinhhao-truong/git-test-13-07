def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
      print(" " * (level * 4) + prefix + str(node.val))
      print_tree(node.left, level + 1, "L--- ")
      print_tree(node.right, level + 1, "R--- ")

class Node:
  def __init__(self, val) -> None:
    self.val = val
    self.right = None
    self.left = None

class BST:
  def __init__(self, val = None) -> None:
    if val:
      self.root = Node(val)
      return
    self.root = None
    
  def insert(self, val):
    self.root = self._insert(self.root, val)
    
  def _insert(self, node, val):
    if not node:
      return Node(val)
    if val < node.val:
      node.left = self._insert(node.left, val)
    else:
      node.right = self._insert(node.right, val)
    return node

  def search(self, val):
    return self._search(self.root, val)
  
  def _search(self, node, val):
    if not node:
      return None
    if node.val == val:
      return node
    if val < node.val:
      return self._search(node.left, val)
    return self._search(node.right, val)
      
  
my_bst = BST(12)
my_bst.insert(13)
my_bst.insert(10)
my_bst.insert(12)
my_bst.insert(19)
my_bst.insert(1)

print_tree(my_bst.root)
print_tree(my_bst.search(9))