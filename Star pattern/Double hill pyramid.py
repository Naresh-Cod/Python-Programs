"""
    *         *
   * *       * *
  * * *     * * *
 * * * *   * * * *
* * * * * * * * * *
"""
star = 5
for row in range(1, star + 1):
    for space in range(star - row):
        print(" ", end="")

    for col in range(row):
        print("*", end=" ")

    for space in range(star - row):
        print(" ", end=" ")

    for col in range(row):
        print("*", end=" ")
    print()