def longest_unique_substring(s):
    seen = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length
print(longest_unique_substring("abcabcbb"))  # Output: 3
