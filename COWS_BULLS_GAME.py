# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 07:27:19 2022

@author: Amulyam
"""



import random
import pyttsx3 as pt


text=pt.init()
l=[1,2,3,4,5,6,7,8,9]
n=random.sample(l,4)
s=''
for i in range(len(n)):
    s=s+str(n[i])
#print(s)
text.say("enter 4 numbers from 0 to 9")
text.runAndWait()
print("ATTEMPT 1")
num=input("enter 4 numbers from 0 to 9 ")
cow=0
bull=0  
for j in range(10):
    for k in range(4):
        if num[k]==s[k]:
            bull+=1
            cow+=1
        elif num[k] in s:
            cow+=1
        else:
            pass
    if cow==4 and bull==4:
        text.say("cows are "+str(cow)+" bulls are "+str(bull))
        text.runAndWait()
        print("cows are ",cow," bulls are ",bull)
        text.say("yes you got the code which is "+s)
        text.runAndWait()
        print("yes you got the code which is ",s)
        text.say("YOU WON your score is "+str(j+1)+" attempts")
        text.runAndWait()
        print("YOU WON")
        print("your score is ",j+1," attempts")
        break
    elif j==9 and cow!=4:
        text.say("cows are "+str(cow)+" bulls are "+str(bull))
        text.runAndWait()
        print("cows are ",cow," bulls are ",bull)
        text.say("GAME OVER"+"the code was "+s)
        text.runAndWait()
        print("GAME OVER",s)
    else:
        text.say("cows are "+str(cow)+" bulls are "+str(bull))
        text.runAndWait()
        print("cows are ",cow," bulls are ",bull)
        text.say("try again. you still have "+str(10-j-1)+" attemps left ")
        text.runAndWait()
        print("try again.you still have ",10-j-1," attemps left ")
        text.say("enter 4 numbers from 0 to 9 ")
        text.runAndWait()
        print("ATTEMPT "+str(j+2))
        new=input("enter 4 numbers from 0 to 9 ")
        num=new
    cow=0
    bull=0
    
        