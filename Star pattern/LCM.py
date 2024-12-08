def find_lcm(a, b):
    # Function to calculate the GCD (Greatest Common Divisor) using Euclidean algorithm
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    # LCM formula: (a * b) // gcd(a, b)
    return (a * b) // gcd(a, b)

# Example usage
num1 = 12
num2 = 18
lcm = find_lcm(num1, num2)
print(f"LCM of {num1} and {num2} is: {lcm}")

def find_gcd(a, b):
    while b:
        a, b = b, a % b  # Update a to b and b to a % b
    return a

# Example usage
num1 = 48
num2 = 18
gcd = find_gcd(num1, num2)
print(f"GCD of {num1} and {num2} is: {gcd}")
