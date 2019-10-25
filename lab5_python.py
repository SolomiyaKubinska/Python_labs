class Student:
    """create an object - student"""
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def get_name(self):
        return self.name

    def get_group(self):
        return self.group

class Work(Student):
    """ srp // work as write an exam"""
    def write_exam(self, exam):
        print(self.get_name() + " write " + exam)

def students():
    st = Student("Anna", "SA-32")
    st1 = Work(st.name, st.group)
    st1.write_exam("OOP")


class Marks:
    """create marks for student"""
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark

class AdditionalMark(Marks):
    """ ocp // good marks = marks + 1"""
    def get_mark(self):
        return super().get_mark() + 5

def marks():
    m = AdditionalMark("Anna", 10)
    print(m.get_name() + " - " + str(m.get_mark()))

class Lipstick:
    """create a lipstick"""
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def application(self):
        pass

class Liquid(Lipstick):
    """lsp // methods for liquid lipsticks"""
    def brush(self):
        print(str(self.get_name()) + " lipstick with brush is " + str(self.color))

    """isp // method for applying a liquid lipstick"""
    def application(self):
        print(str(self.name) + " applies on lips")

class LipBalm(Lipstick):
    """lsp // methods for lip balm"""
    def selfapplied(self):
        print(str(self.get_name()) + " lipstick selfapplied is " + str(self.color))

    """isp // method for applying a lip balm"""
    def application(self):
        print(str(self.name) + " applies on lips")

def lipsticks():
    l1 = Liquid("Kylie", "red")
    l2 = LipBalm("Nivea", "pink")
    """lsp"""
    l1.brush()
    l2.selfapplied()
    """isp"""
    l1.application()
    l2.application()

def main():
    students()
    marks()
    lipsticks()

if __name__ == '__main__':
    main()
