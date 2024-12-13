start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
stap = int(input("Enter a stap number: "))
while start < end:
    sep = start + stap
    start = start + stap
    print(start)
    start += 1

