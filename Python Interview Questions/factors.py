val = int(input("Enter a factors number: "))
for i in range(1, val+1):
    if val % i == 0:
        print(val, f'factors = {i}')