'''f = open('tushar.txt', 'r')
print(f.read())
f.close()

f = open('tushar.txt', 'w')
w = f.write('who are')
f.close()
print(w)

f = open('tushar.txt', 'r+')
r = f.read()
w = f.write('shonu')
f.close()
print(w)

f = open('tushar.txt', 'w+')
r = f.read()
w = f.write('hooo')
f.close()
print(w)
'''
'''with open('tushar.txt', 'r+') as f:
    r = f.read()
print(r)'''

'''with open('tushar.txt', 'r+') as f:
    for i in f:
        print(i)
'''

"""with open('tushar.txt', 'r+') as f:
    print(f.readlines())
"""

"""f = open('tushar.txt', 'w+')
x = f.read()
print(x)
f.write('##')
print(f.tell())
print(x)
f.close()"""

# csv coma saprate value
# helo, hi, hello, word
# TSV, DSV














