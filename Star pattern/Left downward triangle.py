"""
 *****
  ****
   ***
    **
     *
"""
# Use Nested loop

star = 5
for row in range(star + 1):
    for space in range(row):
        print(" ", end="")

    for col in range(star - row):
        print("*", end="")
    print()
