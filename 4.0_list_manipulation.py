"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program uses a list of marketing campaign budgets.

# 2. Process:
# The program displays the list, selects one budget, sorts the budgets and calculates their total.

# 3. Out:
# The program displays the original list, one budget, the sorted list and the total budget.

# 4. What my list is about, and what I computed from it:
# My list contains marketing campaign budgets in euros.
# I calculated the total because it shows the combined budget of all campaigns.


# Your code below

# Create a list of marketing campaign budgets.
budgets = [400, 500, 600, 700, 800, 900, 1000, 1100]

# Print the whole list.
print("All campaign budgets:", budgets)

# Print one item from the list.
print("One campaign budget:", budgets[3])

# Sort the list.
budgets.sort()
print("Sorted budgets:", budgets)

# Calculate the total of all budgets.
total = sum(budgets)
print("Total budget:", total)