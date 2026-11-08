"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In: Four permissions, each stored as one bit.
# 2. Process: Combine two permissions, then check if a third one is there and finally 
# add it and remove one.
# 3. Out: The permission value in binary after each step.
# 4. My permissions are about a company's supplier invoices in a finance team.
# VIEW means you can see the invoice, CREATE means you can enter a new invoice,
# APPROVE means you can accept it for payment and PAY means you can send the payment.
 
# Your code below
 
# Each permission gets its own bit
VIEW    = 0b0001
CREATE  = 0b0010
APPROVE = 0b0100
PAY     = 0b1000
 
# Step 1: Give an accountant VIEW and CREATE
perms = VIEW | CREATE
print("Step 1: VIEW + CREATE      ->", format(perms, "04b"))
 
# Step 2: Check if APPROVE is there
has_approve = (perms & APPROVE) != 0
print("Step 2: Has APPROVE?       ->", has_approve)
 
# Step 3: Add APPROVE
perms = perms | APPROVE
print("Step 3: Add APPROVE        ->", format(perms, "04b"))
 
# Step 4: Remove CREATE
perms = perms & ~CREATE
print("Step 4: Remove CREATE      ->", format(perms, "04b"))

# Comments: Reading the bits from right to left, the final value 0101 means the 
# accountant can now view and approve invoices, but can no longer create them or pay 
# them.