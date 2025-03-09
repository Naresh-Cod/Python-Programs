import random

def prisoners_and_candies(prisoners=100):
    leader = 0  # Leader will count how many have taken candies
    seen = set()  # To keep track of prisoners who have taken candies
    days = 0

    while len(seen) < prisoners - 1:  # Leader doesn't count themselves
        days += 1
        chosen = random.randint(1, prisoners - 1)  # Random prisoner gets candies
        
        if chosen not in seen:  # If new prisoner, leader counts them
            seen.add(chosen)
            leader += 1

    print(f"All prisoners received candies in {days} days.")

prisoners_and_candies()
