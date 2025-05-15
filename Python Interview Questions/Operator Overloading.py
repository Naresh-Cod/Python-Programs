class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  # Overloading `+` operator
        return Number(self.value + other.value)

n1 = Number(10)
n2 = Number(20)

result = n1 + n2  # Internally calls n1.__add__(n2)
print(result.value)  # Output: 30