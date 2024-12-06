def prime(val):
    for i in range(2, val):
        if val % i == 0:
            break

    else:
        print("prime", val)

for usr in range(2, 21):
    prime(usr)


# ----------------------------------------

prime_val = set()

def prime(val):
    for i in range(2, val):
        if val % i == 0:
            break
    else:
        prime_val.add(val)

N = 5

num = 2
while len(prime_val) < N:
    prime(num)
    num += 1

print("Pehle", N, "prime numbers:", prime_val)
