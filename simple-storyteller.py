# Story Generator Documentation:
# This program allows users to create a story by filling in placeholders (variables) in a predefined story template.
# It prompts the user for words based on specific keywords (e.g., noun, pronoun, verb, adjective) to fill in the placeholders.
# -> For template use for example <noun> or <name> in your own story
# Once all placeholders are filled, it generates the complete story and outputs it to a new file.

print("Let's write a story together!")

# Try to open the story file
try:
    file = open("beginner-projects/story.txt", "r")
    lines = file.readlines()
except: 
    print("File does not exist.")

# Print the original story template
for line in lines:
    print(line)

# Define variables to store user inputs for placeholders
storyname = input("What name should your story have? ")
name = input("What name do you want to have? ")
nouns = []
pronouns = []
verbs = []
adjectives = []

# Iterate over each line in the story template
for line in lines:
    
    # Check for placeholders and prompt user for input accordingly
    if "<noun>" in line:
        nouns.append(input("Give me a noun: "))
        print()
    if "<pronoun>" in line:
        pronouns.append(input("Give me a pronoun: "))
        print()
    if "<verb>" in line:
        verbs.append(input("Give me a verb: "))
        print()
    if "<adjective>" in line:
        adjectives.append(input("Give me an adjective: "))
        print()
try:
    # Using open() function
    newfile = "beginner-projects/" + str(storyname) + ".txt"

    # Open the file in write mode
    with open(newfile, 'w') as file:
        # Print the story with user inputs
        print("STORYTIME")
        print()

        # Replace placeholders in the story template with user inputs and print the complete story
        for line in lines:
            line = line.replace("<name>", name)
            line = line.replace("<noun>", "{}").replace("<pronoun>", "{}").replace("<verb>", "{}").replace("<adjective>", "{}")
            # Write content to the file
            file.write(line.format(*nouns, *pronouns, *verbs, *adjectives))
            # Print content to user
            print(line.format(*nouns, *pronouns, *verbs, *adjectives))

        # Print the end of the story
        print()
        print("THE END")
        print()
        print()
        print(f"Your story '{newfile}' is created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")