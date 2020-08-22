'''
Tocheck if the tree is a BST or not
The question can be found here:
https://www.hackerrank.com/challenges/is-binary-search-tree
'''

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def easy(root,listi):
    if root:
        easy(root.left,listi)
        listi.append(root.data)
        easy(root.right,listi)
    return listi
def check_binary_search_tree_(root):
    listi=[]
    duplicates={}
    res=easy(root,listi)
    for i in range(len(res)):
        if res[i] not in duplicates:
            duplicates[res[i]]=1
        else:
            return False
    if res == sorted(res):
        return True
    else:
        return False