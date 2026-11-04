# Name: Stina Nurminen
# Group: CL09
#
# # 1. WHAT GOES IN?
#    My program reads csv file called scenarios_A.csv, where the values are separated by
#    commas. Each line is one situation with 14 columns: the ID, the
#    situation, the three options and for each option the budget change,
#    the reputation change and a feedback message. The numbers are simple
#    whole numbers like -800 or 15. To find the impact of option B, I look
#    at the columns BudgetB and ReputationB.
#
# 2. WHAT HAPPENS IN ONE DAY?
#    The game shows the day, the budget, the reputation, the situation and
#    the three options. The player types A, B or C and the game asks again
#    if the answer is wrong. Then the budget and reputation change, the
#    feedback is shown and the day is saved in the history. If a gauge
#    reaches 0 or less, the player is fired and the game stops.
#
# 3. WHAT COMES OUT?
#    At the end the player sees if they were fired and why or their score
#    and title, together with their best and worst move. One line is added
#    to results.csv, for example: Lea,6350,100,CMO Material,2026-11-03
#
# 4. WHAT COULD GO WRONG?
#    If the player types a wrong letter, the game asks again. If the
#    reputation goes above 100, I set it back to 100. If the budget or the
#    reputation goes to 0 or less, the game stops right away. If the csv
#    file is missing, the program shows a message instead of crashing.
#
# MY FEATURE: d (Difficulty)
#    The player chooses easy (15,000 EUR) or hard (6,000 EUR) at the start.
#    I chose it because it is simple to build but changes the whole game.

import csv
import random
from datetime import date

FILE_NAME = "scenarios_A.csv"
RESULTS_FILE = "results.csv"
DAYS = 10


# Let's read the csv file and save every situation in a list.
# Each option is stored as a tuple with its text, budget change,
# reputation change and feedback message.
def load_scenarios(file_name):
    scenarios = []
    with open(file_name, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            options = {}
            for letter in ["A", "B", "C"]:
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter],
                )
            scenarios.append((row["Scenario"], options))
    return scenarios


# Now let's ask the player if they want easy or hard mode,
# and give them the starting budget that goes with it.
def choose_difficulty():
    while True:
        answer = input("Difficulty: easy or hard? ").strip().lower()
        if answer == "easy":
            return 15000
        if answer == "hard":
            return 6000
        print("Please type easy or hard.")


# Let's keep asking the player until they type A, B or C,
# so a wrong answer never breaks the game.
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ["A", "B", "C"]:
        answer = input("Please type A, B or C: ").strip().upper()
    return answer


# Now let's update the budget and the reputation after the choice.
# The reputation can't go over 100, and the function gives back
# both values together as a tuple.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = reputation + reputation_change
    if reputation > 100:
        reputation = 100
    return budget, reputation


# Let's find the title that matches the player's final score.
def get_title(score):
    if score >= 140:
        return "Viral Legend"
    elif score >= 120:
        return "CMO Material"
    elif score >= 95:
        return "Growth Hacker"
    else:
        return "Eternal Intern"


# Finally, let's save the game by adding one new line to results.csv
# with the name, budget, reputation, title and date
def save_result(name, budget, reputation, title):
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, budget, reputation, title, date.today()])


def main():
    # load the file, if it is missing show a message and stop
    try:
        scenarios = load_scenarios(FILE_NAME)
    except FileNotFoundError:
        print("The file", FILE_NAME, "is missing.")
        return

    # ask the name
    name = input("What is your name? ").strip()
    if name == "":
        name = "Player"

    # starting values
    budget = choose_difficulty()
    reputation = 50
    history = []      # one tuple per day: (reputation change, day, option text)
    fired = False
    reason = ""

    # mix the scenarios
    random.shuffle(scenarios)

    # play 10 days
    for day in range(1, DAYS + 1):
        situation, options = scenarios[day - 1]

        # show the day
        print()
        print("--- Day", day, "---")
        print("[Budget:", budget, "EUR | Reputation:", str(reputation) + "/100]")
        print(situation)
        for letter in ["A", "B", "C"]:
            print("  " + letter + ":", options[letter][0])

        # get the choice and apply it
        letter = ask_choice()
        option = options[letter]
        text, budget_change, reputation_change, feedback = option
        budget, reputation = apply_choice(budget, reputation, option)

        # show what happened
        print(feedback)
        print("Budget", budget_change, "EUR, Reputation", reputation_change)

        # save the day in the history
        history.append((reputation_change, day, text))

        # check if the player is fired
        if budget <= 0:
            fired = True
            reason = "You ran out of money."
            break
        if reputation <= 0:
            fired = True
            reason = "Your reputation hit zero."
            break

    # end of the game
    print()
    print("==============================")
    if fired:
        title = "Fired"
        print("You are fired!", reason)
        print("Budget:", budget, "EUR, reputation:", str(reputation) + "/100")
    else:
        score = reputation + budget // 200
        title = get_title(score)
        print("Quarter survived!")
        print("Budget left:", budget, "EUR, reputation:", str(reputation) + "/100")
        print("Final score:", score)
        print(name + ", your title:", title)

    # best move = biggest reputation change, worst move = smallest
    # python compares tuples with the first element first
    best = max(history)
    worst = min(history)
    print()
    print("Best move:  day", best[1], '"' + best[2] + '"', "(" + str(best[0]) + ")")
    print("Worst move: day", worst[1], '"' + worst[2] + '"', "(" + str(worst[0]) + ")")

    # Last step is to save the game into another csv file.
    save_result(name, budget, reputation, title)
    print("Saved in results.csv")


main()