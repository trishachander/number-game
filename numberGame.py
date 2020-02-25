#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random as r
num = r.randint(1,20)
print("guess a number from 1 to 20")

for i in range(1,8):
    print("take a guess")
    n=int(input())
    
    if(n<num):
        print("your guess was too low.")
    elif(n>num):
        print("your guess was too high")
    else:
        break
if(num==n):
    print("good job")

