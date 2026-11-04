"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My function name, and why return rather than print:


# Your code below
def greet():
    print ("Hello, World!")
    print("Hello, World 2!")
print ("Hello, World!")
greet()
greet()

print("-" * 30)

def greet_person(name):
    print("Hello,", name)
    
greet_person("Alice")
greet_person("Bob")

def add(first, second):
    return first + second

result = add(2, 3)
print("2 + 3 =", result)
print("used directly:", add(10, 5) * 2)

print("-" * 30)