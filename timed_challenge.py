# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 2. Running Total with Reset
# Track a running total of values. If a negative number is added, reset the total to 0.
# Input: [5, 7, -1, 3, 2]
# Output: [5, 12, 0, 3, 5]

class RunningTotal:
    def __init__(self):
        self.total = 0
        self.history = []

    def add_value(self, value):
        if value < 0:
            self.total = 0
        else:
            self.total += value

        self.history.append(self.total)
        return self.total

# For testing RunningTotal. Testing only, no error checking for entry is built in. 
def RunningTotal_Tester():
    tracker = RunningTotal()

    while True:
        entry = input("Enter a number: ")
        value = int(entry)

        print("Current total:", tracker.add_value(value))

RunningTotal_Tester()


# 28 minutes
# For this problem I used a list. Lists are great for when you need to add or remove items, I want to keep duplicates, and order isn’t necessarily important. 
# In this scenario, all I needed was to keep a running total of the inputs until a negative number was entered, in which case the self.total was reset to 0.

# I partially chose this problem because I had a project in the past where I needed to keep a running total of a value. 
# I was already familiar with using a method with self.total = x, how to keep adding to it, reset it, and so on. Given the 30 minute time limit, I felt pretty confident in being able to handle this problem with this constraint. 

# While the program works, I did not have time to create any error handling. When prompted to enter a number, returning a blank response, letter, special character, decimal, or anything besides a whole integer results in the program crashing. 
# This is obviously not ideal, since we want to have error handling built into our programs so users don’t experience unexpected crashes. With more time, I would have added this functionality to the code. I think incorporating a ValueError statement to handle edge cases would have helped solve this. 
# Also realizing I sacrificed on commenting. Looking back, I completed what I did in 28 minutes. I should have spent the last 2 minutes fleshing out my comments better.