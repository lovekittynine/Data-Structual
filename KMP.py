#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:41:51 2019

@author: wsw
"""

# KMP matching

def extract_string(string):
  decoded_string = ''
  n = len(string)
  i = 0
  while i<n:
    char = string[i]
    i += 1
    if char != '[' and char != ']':
      decoded_string += char
    elif char == '[':
      num = ''
      while string[i].isdigit():
        num += string[i]
        i += 1
      decoded_string += string[i]*int(num)
      i += 1
  return decoded_string


def get_next(T):
  i = 0
  # post prefix j=-1
  j = -1
  n = len(T)
  next = [-1]
  while i<n-1:
    if j==-1 or T[next[i]]==T[i]:
      j += 1
      next.append(j)
      i += 1
    else:
      j = next[j]
  return next


def kmp_match(S,T):
  n = len(S)
  m = len(T)
  i = 0
  j = 0
  next = get_next(T)
  while i<n and j<m:
    if j==-1 or S[i]==T[j]:
      i += 1
      j += 1
    else:
      j = next[j]
    # note j must greater than m-1(last element index)
    if j>m-1:
      print('index',i-j)
      return
  print('not exists')
  

def kmp_match_reverse(S,T):
  n = len(S)
  m = len(T)
  i = n-1
  j = 0
  next = get_next(T)
  while i<n and j<m:
    if j==-1 or S[i]==T[j]:
      i -= 1
      j += 1
    else:
      j = next[j]
    # note j must greater than m-1(last element index)
    if j>m-1:
      print('index',i)
      return
  print('not exists')
  
  
if __name__ == '__main__':
  a = 'abcf[9r]po[5k]'
  print(extract_string(a))
  T = 'abcd'
  print(get_next(T))
  kmp_match_reverse(S='abcabcdef',T='dcb')