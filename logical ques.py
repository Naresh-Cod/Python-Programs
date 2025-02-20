# Natural number
n = 5
for i in range(n+1):
    print(i)

# factors
n = 12
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
# factorial
n = 4
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

# prime number
n = 30
for i in range(1, n+1):
    if i % 2 != 0:
        print(i, end=' ')

# armstrong
n = 153
n_new = n
val = 0
while n != 0:
    fac = n % 10
    val += fac ** 3
    dev = n // 10
    n = dev
if n_new == val:
    print('This is Armstrong')

# strong number
n = 145
val = 1
strong = 0
while n:
    fac = n % 10
    for i in range(1, fac+1):
        val = val * i
    strong += val
    val = 1
    dev = n // 10
    n = dev
print(strong)
