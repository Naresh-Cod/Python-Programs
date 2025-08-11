def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# List of numbers
nums = [2, 3, 4, 5, 10, 13, 17, 20, 23]

# Filter primes using list comprehension
primes = [x for x in nums if is_prime(x)]

print("Prime numbers in the list:", primes)
