string = input("Enter a string: ")

stack = []

for ch in string:
    stack.append(ch)
reverse = ""
while stack:
    reverse += stack.pop()

print("Reversed string:", reverse)