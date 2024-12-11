class student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        print("student name: ", self.name)
        print("student age: ", self.age)
        print("student marks: ", self.marks)


    def mark(self):
        self.num = self.marks / 500 * 100

        if self.num >= 90:
            print("first div: ", self.num)

        elif self.num <= 90 and self.num >= 60:
            print("Sec div: ", self.num)

        elif self.num <= 60 and self.num >= 40:
            print("third div: ", self.num)

        else:
            print("Fall: ", self.num)

sos = student("sonu", 12, 100)
sos.details()
sos.mark()