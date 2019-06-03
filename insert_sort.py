#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:06:23 2019

@author: wsw
"""

def insert_sort(arr):
  n = len(arr)
  for i in range(1,n):
    if arr[i]<arr[i-1]:
      temp = arr[i]
      for j in range(i-1,-1,-1):
        # put all >= current element(temp) post move
        if arr[j]>=temp:
          arr[j+1]=arr[j]
        else:
          break
      # insert to approprate position
      arr[j+1]=temp
  return arr


def shell_sort(arr):
  n = len(arr)
  # 设置增量
  cremental = n
  while cremental>1:
    # 增量变化
    cremental = cremental//3+1
    for i in range(cremental,n):
      if arr[i]<arr[i-cremental]:
        temp = arr[i]
        j = i-cremental
        while j>=0:
          # 大于当前元素的所有元素后移动cremental个位置
          if arr[j]>=temp:
            arr[j+cremental] = arr[j]
            j -= cremental
          else:
            # 插入
            arr[j+cremental] = temp
            break
        if j<0:
          arr[j+cremental] = temp
  return arr    

if __name__ == '__main__':
  li = [1,8,5,4,2,3,7,6,9]
  # print(insert_sort(li))
  print(shell_sort(li))