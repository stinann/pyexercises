"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

# 1. In: Two values, a and b
# 2. Process: Compare them and then combine the results
# 3. Out: A table of results
# 4. I picked the values 5 which is an integer and 5.0 which is a float. After getting
# the results, I was surprised by the fact that a == b came out as "True", even though 
# the two values have different types. It means that Python compares the numeric value,
# not the type, so 5 and 5.0 count as equal. Because of that, a < b and a > b are both 
# "False", while a <= b and a >= b are both "True".


a = 5
b = 5.0

comparisons = {
    "a == b": a == b,
    "a != b": a != b,
    "a < b":  a < b,
    "a > b":  a > b,
    "a <= b": a <= b,
    "a >= b": a >= b,
}
 
combos = {
    "(a < b) and (a != b)": (a < b) and (a != b),
    "(a < b) or (a == b)":  (a < b) or (a == b),
    "not (a == b)":         not (a == b),
}
 
# Put both groups of results into one list
all_results = list(comparisons.items()) + list(combos.items())
 
# Go through the list one row at a time
for name, result in all_results:
    print(name, "->", result)