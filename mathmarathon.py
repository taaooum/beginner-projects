#Timed Math challange
#random generierte mathe fragen -> bestimme anzahl 
#messe die zeit um die dauer der Fragen zurückzugeben und einen Avarage Score der Ergebnisse

import time
import random

#defines a countdown for t seconds
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end = "\r") 
        time.sleep(1) 
        t -= 1
    print(t)

print("This is a math marathon!")
print("You will have 1 minute to answer as many questions as you can.")
print()

timer = 60 #time in seconds

if input("Are you ready? ").lower() not in ["yes", "y", "yee", "yeah"]:
    print()
    print("I guess this is to hard for you...")
    print("See you next time!")
    quit()

countdown(timer)
