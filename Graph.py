#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:08:47 2019

@author: wsw
"""

# graph

class VertexNode():
  def __init__(self,vertex):
    self.vertex = vertex
    self.firstedge = None

class EdgeNode():
  def __init__(self,adjcent,weight=0):
    self.adjcent = adjcent
    self.weight = weight
    self.next = None
    
class Graph():
  def __init__(self):
    self.vertexs = []
    self.visited = []
    self.numVertexs = 0
    
  def create(self,vertexs,edges):
    self.numVertexs = len(vertexs)
    self.visited = [0]*self.numVertexs
    for vertex in vertexs:
      vertex = VertexNode(vertex)
      self.vertexs.append(vertex)
    for edge in edges:
      i,j,w = edge
      edgenode = EdgeNode(j,w)
      edgenode.next = self.vertexs[i].firstedge
      self.vertexs[i].firstedge = edgenode
      #-----------------------------------
      edgenode = EdgeNode(i,w)
      edgenode.next = self.vertexs[j].firstedge
      self.vertexs[j].firstedge = edgenode
    
  def DFS(self,i):
    """
    recursive bfs traverse
    """
    print(self.vertexs[i].vertex,end=' ')
    self.visited[i] = 1
    edge = self.vertexs[i].firstedge
    while edge is not None:
      k = edge.adjcent
      if self.visited[k] == 0:
        self.DFS(k)
      else:
        edge = edge.next
        
  def DFSIterator(self,i):
    stack = [i]
    while stack:
      k = stack.pop()
      # if self.visited[k] == 0:
      print(self.vertexs[k].vertex,end=' ')
      self.visited[k] = 1
      edge = self.vertexs[k].firstedge
      while edge is not None:
        j = edge.adjcent
        if self.visited[j]==0:
          stack.append(j)
          self.visited[j] = 1
        edge = edge.next
        
  def DFSTraverse(self):
    for i in range(self.numVertexs):
      if self.visited[i]==0:
        self.DFS(i)
    self.visited = [0]*self.numVertexs
    print('')

  def DFSIteratorTraverse(self):
    for i in range(self.numVertexs):
      if self.visited[i]==0:
        self.DFSIterator(i)
    self.visited = [0]*self.numVertexs
    print('')
    
  def BFSTraverse(self):
    for i in range(self.numVertexs):
      if self.visited[i]==0:
        queue = [i]
        while queue:
          cur = queue.pop(0)
          self.visited[cur] = 1
          print(self.vertexs[cur].vertex,end=' ')
          edge = self.vertexs[cur].firstedge
          while edge is not None:
            k = edge.adjcent
            if self.visited[k]==0:
              queue.append(k)
              self.visited[k]=1
            edge = edge.next
    print('')
    self.visited = [0]*self.numVertexs
    
  def mini_span_tree_prim(self):
    w = [65535]*self.numVertexs
    w[0] = 0
    edge = self.vertexs[0].firstedge
    self.visited[0] = 1
    cost = 0
    vertexs = [0]*self.numVertexs
    while edge is not None:
      k = edge.adjcent
      d = edge.weight
      w[k] = d
      edge = edge.next
    for i in range(1,self.numVertexs):
      min_cost = 65535
      k = 0
      for j in range(1,self.numVertexs):
        if self.visited[j]==0 and w[j]<min_cost:
          min_cost = w[j]
          k = j
      self.visited[k] = 1
      cost += min_cost
      print('%s->%s'%(vertexs[k],k),end=' ')
      edge = self.vertexs[k].firstedge
      while edge is not None:
        j = edge.adjcent
        d = edge.weight
        if self.visited[j]==0 and d<w[j]:
          w[j] = d
          vertexs[j] = k
        edge = edge.next
    print('min cost',cost)
    
if __name__ == '__main__':
  graph = Graph()
  vertexs = list('ABCDEFGHI')
  edges = [(0,1,10),(1,2,18),(2,3,22),(3,4,20),(4,5,26),
           (5,0,11),(5,6,17),(6,7,19),(6,3,24),(6,1,16),
           (7,3,16),(7,4,7),(1,8,12),(2,8,8),(3,8,21)]
  graph.create(vertexs,edges)
  graph.DFSTraverse()
  graph.DFSIteratorTraverse()
  graph.BFSTraverse()
  graph.mini_span_tree_prim()