# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 08:59:58 2022

@author: 24MarcusL
"""
import easygui
import tkinter as tk
from tkinter import ttk
import sys
import csv
import re


LARGE_FONT= ("Verdana", 50)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=100, padx = 100)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


lang = open('table.csv', 'r')
content = lang.read()

l = content.split(",")
l.remove("ï»¿a")

arr = []
arrPart = []
i = 0

for line in l:
    if i > 14:
        arr.append(arrPart)
        arrPart = []
        i = 0
    line = line.replace("%", "")
    line = line.replace("\n", "")
    line = line.replace("*", "")
    line = re.sub("[a-zA-z]", "", line)
    arrPart.append(float(line))
    i = i + 1
    
arr.append(arrPart) #for the "z" row of the table
#print(arr)

#Next Part: calculating the number of occurances for each letter
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
occurr = [0.0]*26

inp = easygui.enterbox("Please input a text of any language: ")

numLetters = 0;
for char in inp:
    char = char.lower()
    if re.search("[a-zA-Z]", char) == None:
        continue
    elif char == "İ".lower():
        continue
    numLetters = numLetters + 1
    occurr[letters.index(char)] = occurr[letters.index(char)] + 1.0


for i in range(26):
    occurr[i] = occurr[i]/numLetters * 100
        
    

score = 100
index = 0
finalIndex = 0

for i in range(15):
    currScore = 0
    for j in range(26):
        currScore = currScore + ((occurr[j] - arr[j][i])**2)
    if currScore < score:
        score = currScore
        finalIndex = index
    index = index + 1
    
if finalIndex == 0:
    popupmsg("English")  
elif finalIndex == 1:
    popupmsg("French")  
elif finalIndex == 2:
    popupmsg("German")  
elif finalIndex == 3:
    popupmsg("Spanish")  
elif finalIndex == 4:
    popupmsg("Portuguese")  
elif finalIndex == 5:
    popupmsg("Esperanto")  
elif finalIndex == 6:
    popupmsg("Italian")  
elif finalIndex == 7:  
    popupmsg("Turkish")  
elif finalIndex == 8:
    popupmsg("Swedish")  
elif finalIndex == 9:
    popupmsg("Polish")  
elif finalIndex == 10:
    popupmsg("Dutch")  
elif finalIndex == 11:
    popupmsg("Danish")  
elif finalIndex == 12:
    popupmsg("Icelandic")  
elif finalIndex == 13:
    popupmsg("Finnish")  
elif finalIndex == 14:
    popupmsg("Czech")  


