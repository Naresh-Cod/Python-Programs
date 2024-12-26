class Test:
    x = 10  #static variable
    def __init__(self, name):   #instance member function
        self.name = name    #instance member variable

t1 = Test('sam')    #Test = class object
print(type(t1))     #t1 = instance member variable
