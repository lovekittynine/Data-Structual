#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:15:01 2019

@author: wsw
"""

# binary search
import time

def binary_search(arr,left,right,target):
  """
  递归实现二分查找算法：
  需要注意调用递归函数的时候需要返回值(return)
  """
  if left<=right:
    mid = (left+right)//2
    if arr[mid]==target:
      return mid
    elif arr[mid]>target:
      return binary_search(arr,left,mid-1,target)
    else:
      return binary_search(arr,mid+1,right,target)
  else:
    return -1
  
if __name__ == '__main__':
  arr = list(range(100000000))
  target = 200
  start = time.time()
  print(binary_search(arr,0,len(arr)-1,target))
  end = time.time()
  print('Time Cosumed:%.6fSec'%(end-start))
  
