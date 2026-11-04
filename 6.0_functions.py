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

# 1. In: I used the list of marketing campaign budgets in euros, which I created
# previously in exercise 4.0.
#
# 2. Process: The function adds up the budgets and divides the total
# by the number of campaigns.
#
# 3. Out: The average budget per campaign in euros.
#
# 4. My function: It is called "average_budget". It tells exactly what it returns:
# the average budget of the campaigns in the list.
#
# Why return rather than print: A returned value can be stored in a
# variable, compared, or used in further calculations. For example
# to check whether a new campaign is above or below average.
# A printed value only appears on the screen and the program
# can't use it anymore.
#
# Empty list check: Function "average_budget()" returns 0 instead of crashing.
# Without the check, Python would divide by zero and raise an error.
# I think returning 0 is acceptable, because no campaigns means no
# money spent per campaign. However, it could be misleading in a report,
# so it should be explained there.


budgets = [400, 500, 600, 700, 800, 900, 1000, 1100]


def average_budget(budget_list):
    """Returns the average campaign budget, or 0 for an empty list."""
    if len(budget_list) == 0:
        return 0
    return sum(budget_list) / len(budget_list)


# Three calls with different inputs
all_campaigns = average_budget(budgets)          # all eight campaigns
small_campaigns = average_budget(budgets[:4])    # the four smallest
no_campaigns = average_budget([])                # empty list

print("Average budget, all campaigns:", all_campaigns, "€")
print("Average budget, smallest four:", small_campaigns, "€")
print("Average budget, no campaigns:", no_campaigns, "€")