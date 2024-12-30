class Test:
    def __init__(self): #instance function
        self.a = 5  #instance member variable
    def f1(self):
        self.b = 10

t1= Test() #instance object
t2 = Test()

t1.f1()
t1.c = 15

print(t1.__dict__)