class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Branch:", self.branch)


s1 = Student("Soumya", "CSE")
s2 = Student("vidya", "ECE")

s1.display()
print()
s2.display()