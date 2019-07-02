#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:00:58 2019

@author: wsw
"""
"""
求一个入栈序列的所有可能出栈序列
"""

def get_permutation(sequence):
  """
  返回一个序列的全排列(回溯法)
  """
  output = []
  n = len(sequence)
  def backtrace(cur=[],nums=[]):
    if len(cur)==n:
      output.append(cur[:])
      return 
    for i in range(len(nums)):
      cur.append(nums[i])
      backtrace(cur,nums[:i]+nums[i+1:])
      cur.pop()
  backtrace([],sequence[:])
  return output


def validPopSequence(pushed,popped):
  """
  判断一个序列是否是入栈序列的一个出栈序列
  """
  n = len(pushed)
  j = 0
  stack = []
  for i in range(n):
    stack.append(pushed[i])
    while stack and stack[-1]==popped[j]:
      stack.pop()
      j += 1
  while j<n:
    if stack[-1]==popped[j]:
      j += 1
      stack.pop()
    else:
      return False
  return True


if __name__ == '__main__':
  pushed = [1,2,3,4,5,6,7,8,9,10]
  permutations = get_permutation(pushed)
  output = []
  for permutation in permutations:
    if validPopSequence(pushed,permutation):
      output.append(permutation)
  print(output)
