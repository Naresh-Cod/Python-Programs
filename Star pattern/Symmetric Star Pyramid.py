"""
*
**
***
****
***
**
*
"""

star = 7
for i in range(1, star+1):
    if i != 5 and i != 6 and i != 7:
        for j in range(i):
            print(j, end='')
    else:
        for p in range(8-i):
            print(p, end='')
    print()

print()