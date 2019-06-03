#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:54:27 2019

@author: wsw
"""

class Node():
  def __init__(self,data):
    self.data = data
    self.lchild = None
    self.rchild = None
    

class Tree():
  def __init__(self):
    self.root = None
  
  def create(self,item):
    node = Node(item)
    queue = [self.root]
    if self.root is None:
      self.root = node
      return
    
    while queue:
      cur = queue.pop(0)
      if cur.lchild is None:
        cur.lchild = node
        return
      else:
        queue.append(cur.lchild)
      if cur.rchild is None:
        cur.rchild = node
        return
      else:
        queue.append(cur.rchild)
      
  def preOrderTraverse(self,root):
    stack = [root]
    while stack:
      cur = stack.pop()
      print(cur.data,end=' ')
      if cur.rchild is not None:
        stack.append(cur.rchild)
      if cur.lchild is not None:
        stack.append(cur.lchild)
    print('')
  
  def BFSTraverse(self,root):
    queue = [root]
    while queue:
      cur = queue.pop(0)
      print(cur.data,end=' ')
      if cur.lchild is not None:
        queue.append(cur.lchild)
      if cur.rchild is not None:
        queue.append(cur.rchild)
    print('')
    
  def postOrderTraverse(self,root):
    stack = [root]
    res = []
    while stack:
      cur = stack.pop()
      res.append(cur.data)
      if cur.lchild is not None:
        stack.append(cur.lchild)
      if cur.rchild is not None:
        stack.append(cur.rchild)
    while res:
      print(res.pop(),end=' ')
    print('')
    
  def midOrderTraverse(self,root):
    stack = [root]
    while root is not None and stack:
      while root.lchild is not None:
        stack.append(root.lchild)
        root = root.lchild
      if stack:
        root = stack.pop()
        print(root.data,end=' ')
        if root.rchild is not None:
          stack.append(root.rchild)
          root = root.rchild
    print('')
      
      
    
    
if __name__ == '__main__':
  tree = Tree()
  nodes = [1,2,3]
  for node in nodes:
    tree.create(node)
  tree.BFSTraverse(tree.root)
  tree.preOrderTraverse(tree.root)
  tree.postOrderTraverse(tree.root)
  tree.midOrderTraverse(tree.root)