glo = 10 #global variable
def f1():
    loc = 20 #local variable
    global glo
    print(glo)
    print(loc)
f1()

