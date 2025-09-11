def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print("Is 29 prime?", is_prime(29))  # True
print("Is 20 prime?", is_prime(20))  # False
