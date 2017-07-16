# -*- coding: utf-8 -*-
import time
import webbrowser

twoHours = 7200

print("This program started on " + time.ctime())
for x in range(3):
    time.sleep(twoHours)
    webbrowser.open("https://www.youtube.com/watch?v=zBRG-nNErkQ")
    
