# create a function mistake n value as number of rows and have to print a pyramid

def pyramid(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
nums = int(input("Enter pyramid Row: "))
pyramid(nums)