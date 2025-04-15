# Base class
class Grandfather:
    def show_grandfather(self):
        print("I am the grandfather.")

# Derived from Grandfather
class Father(Grandfather):
    def show_father(self):
        print("I am the father.")

# Derived from Father
class Son(Father):
    def show_son(self):
        print("I am the son.")

# Create object of Son
s = Son()
s.show_grandfather()  # Inherited from Grandfather
s.show_father()       # Inherited from Father
s.show_son()          # From Son class
