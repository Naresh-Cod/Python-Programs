"""
0
0 1
0   2
0     3
0   2
0 1
0
"""
rows = 4

for i in range(1, rows + 1):
    for j in range(i):
        if j == 0 or j == i-1:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()

for i in range(rows-1, 0, -1):
    for j in range(i):
        if j == 0 or j == i-1:
            print(j, end=' ')
        else:
            print(" ", end=' ')
    print()