from collections import Counter

def char_count(s):
    return Counter(s)

# Example
print(char_count("banana"))
# Output: Counter({'a': 3, 'n': 2, 'b': 1})
