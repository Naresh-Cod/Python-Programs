class Test:
    a = 5 #static variable
    def __init__(self, a):  #instance member function
        self.a = a  #instance variable
        b = 5   # local variable
        Test.p = 5  #static variable

    def test(self):
        self.r = 8

    @staticmethod
    def sam():  #static member function
        Test.ri = 44    #static variable

    @classmethod
    def sam2(sa):
        sa.s = 77

ts = Test(4)

