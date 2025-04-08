numbers = [10, 20, 4, 45, 99]

# Assume the first element is the maximum
maximum = numbers[0]

# Loop through the list
for num in numbers:
    if num > maximum:
        maximum = num

print("The maximum element is:", maximum)
