n = 5
for i in range(1, n+1):
    for j in range(1, n):
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*", end=' ')
    print()
