"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program uses a list of marketing campaign budgets.

# 2. Process:
# The program displays the list in four different orders.
# It uses sorted(), sorted() with reverse=True, reverse() and sort().

# 3. Out:
# The program displays the list in four different orders.
# At the end, it displays the unchanged original list.

# 4. My four orders, and which ones modify the original:
# 1. Ascending order using sorted() - creates a copy.
# 2. Descending order using sorted() - creates a copy.
# 3. Reversed order using reverse() - modifies the list.
# 4. Sorted order using sort() - modifies the list.
# I use copies with reverse() and sort() to protect the original list.


# Your code below

# Create the original list.
budgets = [400, 500, 600, 700, 800, 900, 1000, 1100]

# 1. Sort the list in ascending order.
print("Ascending order:", sorted(budgets))

# 2. Sort the list in descending order.
print("Descending order:", sorted(budgets, reverse=True))

# 3. Reverse a copy of the list.
reversed_budgets = budgets.copy()
reversed_budgets.reverse()
print("Reversed order:", reversed_budgets)

# 4. Sort a copy of the list.
sorted_budgets = budgets.copy()
sorted_budgets.sort()
print("Sorted in place:", sorted_budgets)

# Display the original list at the end.
print("Original list:", budgets)

# CHECK IT YOURSELF / Results:
# Ascending order: [400, 500, 600, 700, 800, 900, 1000, 1100]
# Descending order: [1100, 1000, 900, 800, 700, 600, 500, 400]
# Reversed order: [1100, 1000, 900, 800, 700, 600, 500, 400]
# Sorted order: [400, 500, 600, 700, 800, 900, 1000, 1100]
# Original list: [400, 500, 600, 700, 800, 900, 1000, 1100]
# The original list remains unchanged.