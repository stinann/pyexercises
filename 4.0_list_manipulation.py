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
# Empty list check: Function "average_budget()"" returns 0 instead of crashing.
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