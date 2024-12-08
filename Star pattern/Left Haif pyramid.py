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
    for space in range(star - row):
        print(' ', end='')

    for col in range(1, row + 1):
        print('*', end='')
    print()