class MonkeyPatching:
    def __init__(self, app):
        self.app = app
    @staticmethod
    def gat_data():
        print("Some code to fetch data from database")

    def f1(self):
        self.gat_data()
    def f2(self):
        self.gat_data()

test = MonkeyPatching(5)
test.f1()
test.f2()

def new_get_data(self):
    print("Some code to fetch data from test data")

MonkeyPatching.gat_data = new_get_data
print()
test.f1()
test.f2()