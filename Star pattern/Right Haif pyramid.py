"""
    *
    **
    ***
    ****
    *****
"""
# Use Nested loop

star = 5
for row in range(1, star + 1):
    for col in range(1, row + 1):
        print('*', end='')
    print()