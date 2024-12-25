def even_number(n):
    i = 1
    while n:
        yield 2 * i
        i += 1
        n -= 1
it = even_number(10)
print(type(it))
even_list = []
while True:
    try:
        even_list+=[next(it)]
    except StopIteration:
        break
print(even_list)

