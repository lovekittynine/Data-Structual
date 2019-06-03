#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:47:47 2019

@author: wsw
"""

from collections import deque

class BiTreeNode():
  def __init__(self,data):
    self.data = data
    self.lchild = None
    self.rchild = None

    
class BiTree():
  def __init__(self):
    self.root = None
  
  def search(self,item):
    cur = self.root
    p = None
    while cur is not None:
      if cur.data == item:
        return True,cur
      elif cur.data>item:
        p = cur
        cur = cur.lchild
      else:
        p = cur
        cur = cur.rchild
    return False,p
  
  def insert(self,item):
    # search
    flag,p = self.search(item)
    if not flag:
      node = BiTreeNode(item)
      if p is None:
        self.root = node
      elif p.data>item:
        p.lchild = node
      else:
        p.rchild = node
  
  def midOrderTraverse(self,root):
    if root is None:
      return
    self.midOrderTraverse(root.lchild)
    print(root.data,end=' ')
    self.midOrderTraverse(root.rchild)
    
  def preOrderTraverse(self,root):
    if root is None:
      return
    print(root.data,end=' ')
    self.preOrderTraverse(root.lchild)
    self.preOrderTraverse(root.rchild)
    
  def preOrderTraverseIterator(self,root):
    """
    using stack to implement preordertraverse
    note : we add right child firstly,and then
           add left child
    """
    stack = [root]
    while stack:
      cur = stack.pop()
      print(cur.data,end=' ')
      if cur.rchild is not None:
        stack.append(cur.rchild)
      if cur.lchild is not None:
        stack.append(cur.lchild)
    print('')
    
  def postOrderTraverseIterator(self,root):
    stack = [root]
    res = []
    while stack:
      cur = stack.pop()
      res.append(cur.data)
      if cur.lchild is not None:
        stack.append(cur.lchild)
      if cur.rchild is not None:
        stack.append(cur.rchild)
    # print res
    while res:
      node = res.pop()
      print(node,end=' ')
    print('')
    
  def midOrderTraverseIterator(self,root):
    stack = []
    while True:
      # add root all left child
      while root is not None:
        stack.append(root)
        root = root.lchild
      # print node and if rchild is exists
      # then ready to add to stack
      if stack:
        cur = stack.pop()
        print(cur.data,end=' ')
        root = cur.rchild
      if len(stack)==0 and root is None:
        print('')
        return
    
  def is_Balanced(self):
    queue = deque([self.root])
    while queue:
      cur = queue.popleft()
      left_bf = 0
      right_bf = 0
      
      if cur.lchild is not None:
        queue.append(cur.lchild)
        left_sub_tree = [cur.lchild]
        while left_sub_tree:
          left_num = len(left_sub_tree)
          left_bf += 1
          while left_num>0:
            node = left_sub_tree.pop(0)
            left_num -= 1
            if node.lchild is not None:
              left_sub_tree.append(node.lchild)
            if node.rchild is not None:
              left_sub_tree.append(node.rchild)
       
      if cur.rchild is not None:
        queue.append(cur.rchild)
        right_sub_tree = [cur.rchild]
        while right_sub_tree:
          right_num = len(right_sub_tree)
          right_bf += 1
          while right_num>0:
            node = right_sub_tree.pop(0)
            right_num -= 1
            if node.lchild is not None:
              right_sub_tree.append(node.lchild)
            if node.rchild is not None:
              right_sub_tree.append(node.rchild)
      # print('left tree bf-right tree bf:',left_bf,right_bf)
      if abs(left_bf-right_bf)>1:
        return False
    return True


if __name__ == '__main__':
  nodes = [4,2,1,3,7,6,5,9,8,10]
  bitree = BiTree()
  for node in nodes:
    bitree.insert(node)
  bitree.midOrderTraverse(bitree.root)
  print('')
  bitree.preOrderTraverse(bitree.root)
  print('')
  bitree.preOrderTraverseIterator(bitree.root)
  print(bitree.is_Balanced())
  bitree.postOrderTraverseIterator(bitree.root)
  bitree.midOrderTraverseIterator(bitree.root)