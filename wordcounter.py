#!/usr/bin/env python3

from easygui import *
from collections import Counter
import string

userText = textbox()
translation_table = str.maketrans('', '', string.punctuation)
userText = userText.lower()
userText = userText.translate(translation_table)
print("Words found: ")
print(userText)
userTextList = userText.split()
print("Word list: ")
print(userTextList)
userTextFrequency = Counter()
for i in userTextList:
    userTextFrequency[i] += 1
print(userTextFrequency)
msgbox(userTextFrequency.most_common(50))