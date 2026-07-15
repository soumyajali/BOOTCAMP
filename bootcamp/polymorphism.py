class Num:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Num(self.value + other.value)

    def __str__(self):
        return str(self.value)

n1 = Num(10)
n2 = Num(20)

print(n1 + n2)