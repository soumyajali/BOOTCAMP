class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print(f"Pushed: {value}")

    def pop(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            print(f"Popped: {self.items.pop()}")

    def isEmpty(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")
    def isFull(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            print("Stack is Not Empty")

    def size(self):
        print("Size:", len(self.items))

    def display(self):
        if len(self.items) == 0:
            print("Stack is Empty")
        else:
            print("Stack:", self.items)


s = Stack()

s.push(90)
s.push(89)
s.push(90)

s.display()