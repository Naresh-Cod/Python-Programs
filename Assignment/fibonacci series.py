# write a program to create input user 10 digits number for fibonacci series and return list value

def fibonacci(nums):
    n = -1
    p = 1
    start = 0
    lis1 = []
    while start <= nums:
        val = n + p
        n = p
        p = val
        start = start + 1
        lis1.append(val)
    return lis1
li = fibonacci(int(input("Enter fibonacci series: ")))
print(li)
