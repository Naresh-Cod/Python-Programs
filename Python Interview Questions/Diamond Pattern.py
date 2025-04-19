num = 5
for i in range(1, num + 1):
    for space in range(num, i, -1):
        print(' ', end='')
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
for i in range(1, num):
    for space in range(i):
        print(' ', end='')
    for j in range(num-1, i - 1, -1):
        print(j, end=' ')
    print()
