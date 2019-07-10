#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:06:37 2019

@author: wsw
"""

import numpy as np
np.random.seed(1)

li = np.random.randint(0,100,10).tolist()

def get_partition(li,low,high):
  pivot = li[low]
  while low<high:
    while low<high and li[high]>=pivot:
      high -= 1
    li[low],li[high] = li[high],li[low]
    while low<high and li[low]<pivot:
      low += 1
    li[low],li[high] = li[high],li[low]
  return low


def quick_sort(li,low,high):
  if low<high:
    mid = get_partition(li,low,high)
    quick_sort(li,low,mid-1)
    quick_sort(li,mid+1,high)


def find_topk(li,low,high,k=5):
  if low<high:
    mid = get_partition(li,low,high)
    if mid==k:
      return
    elif mid<k:
      find_topk(li,mid+1,high)
    else:
      find_topk(li,low,mid-1)
    
    
if __name__ == '__main__':
  print('before:',li)
  quick_sort(li,0,9)
  print('after:',li)
  find_topk(li,0,9,5)
  print(li[:5])
  
  