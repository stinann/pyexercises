"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The user enters a sentence.

# 2. Process:
# The program changes the sentence in four different ways.

# 3. Out:
# Four different versions of the sentence.

# 4. My four transformations, and when each is useful:
# upper(): Useful when I want all letters to be capital letters.
# lower(): Useful when I want all letters to be small letters.
# strip(): Useful when I want to remove extra spaces from the beginning and end.
# title(): Useful when I want the first letter of each word to be capitalized.


# Your code below

# Ask the user to enter a sentence.
sentence = input("Enter a sentence: ")

# Change all letters to uppercase.
print("Uppercase:", sentence.upper())

# Change all letters to lowercase.
print("Lowercase:", sentence.lower())

# Remove extra spaces from the beginning and end.
print("Strip:", sentence.strip())

# Make the first letter of each word uppercase.
print("Title:", sentence.title())

# Results/ Check it yourself:
Uppercase:   TODAY IS FRIDAY  
Lowercase:   today is friday  
Strip: today Is friday
Title:   Today Is Friday 

# The results were as expected.
