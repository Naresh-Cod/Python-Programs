"""
 *****
 ****
 ***
 **
 *
"""
# Use Nested loop

star = 5
for row in range(star + 1, 1, -1):
    for col in range(row - 1):
        print('*', end='')
    print()