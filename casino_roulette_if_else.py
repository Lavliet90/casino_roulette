#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
On the roulette wheel, the pockets are numbered from 0 to 36. Below are the colors of the pockets:
pocket 0 green;
for pockets 1 to 10, odd numbered pockets are red, even numbered pockets black;
for pockets 11 to 18, odd numbered pockets are black, even numbered pockets red;
for pockets 19 to 28, odd numbered pockets are red, even numbered pockets black;
for pockets 29 to 36, the odd numbered pockets are black, the even numbered pockets red.

Write a program that reads the pocket number and indicates whether the pocket is green, red, or black. 
The program should display an error message if the user enters a number that is outside the range from 0 to 36.
'''


a=int(input())
if (10>=a>=1 or 28>=a>=19) and a%2==0:
    print("черный")
elif (10>=a>=1 or 28>=a>=19) and a%2==1:
    print("красный")
elif a==0:
    print("зеленый")
elif (11<=a<=18 or 29<=a<=36) and a%2==0:
    print("красный")
elif (11<=a<=18 or 29<=a<=36) and a%2==1:
    print("черный")
else:
    print("ошибка ввода")
    
