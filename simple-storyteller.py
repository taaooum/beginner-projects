#Story Generator, lege einetxt ab die eine Story mit variabeln enthält
#frage den Spieler nach wörtern mit bestimmten keywords (verb, gefühl-...) <Verb> -> wort das ersetzt wird
#füge die Variabeln in die Story und gebe diese aus in einer neuen txt und lege sie ab


print("Lets write a story together!")

if input("Are you ready? ") in ["n", "N", "no", "No"]:
    quit()

print("then lets begin")

file = open("story.txt", "r")
lines = file.readlines()
print(lines)