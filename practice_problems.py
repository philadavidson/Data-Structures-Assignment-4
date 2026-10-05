"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
        return len(product_ids) != len(set(product_ids))

# Why it fits and expected runtime?
# Sets are perfrect for this since they only store unqie product IDs. 
# So determine if there are any duplicates we compare the length of the product ID set with the orifinal collection's length.
# (Just learned about O(n) and O(1)) Creating this set takes O(n) expected runtime and then comparing the lengths takes O(1).


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next

        if not self.front:
            self.rear = None 
        return removed_node.value

# Why it fits and expected runtime?
# A queue fits here because it is asking for first in, first out (FIFO). 
# Adding items to the end or removing them should both take O(1) time since the queue is maintaining references at both ends.

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(set(self.values))

# Why it fits and expected runtime?
# A set fits here because it only keeps unique integer values, repeats are ignored. 
# Adding a value would take O(1) time and returning the count with len() should also take O(1) time.