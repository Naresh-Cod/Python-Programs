sti = "hey hello tushar hey"
mydic = {}
for i in sti.split(' '):
    mydic[i] = 1
    if i not in mydic:
        mydic[i] = 1
    else:
        mydic[i] = mydic[i] + 1
print(mydic)
