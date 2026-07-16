class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        print(f"{value} pushed into stack.")

    def pop(self):
        if len(self.items) == 0:
            print("Stack Underflow! Stack is empty.")
        else:
            print(f"{self.items.pop()} popped from stack.")

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty.")
        else:
            print("Top element:", self.items[-1])

    def display(self):
        if len(self.items) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements (Top to Bottom):")
            for i in range(len(self.items) - 1, -1, -1):
                print(self.items[i])

    def isEmpty(self):
        if len(self.items) == 0:
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
 
stack = Stack()

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Is Empty")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element to push: "))
        stack.push(value)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        stack.isEmpty()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")