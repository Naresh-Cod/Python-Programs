def find_unique(nums):
    freq = {}

    # Count frequency of each number
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    # Find the number that occurs only once
    for n in nums:
        if freq[n] == 1:
            return n

# Example
print(find_unique([3, 3, 3, 7, 3, 3]))
# Output: 7
