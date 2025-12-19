stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(f"before pop {stack}")

removed_element = stack.pop()
print(f"removed element {removed_element}")
print(f"after pop {stack}")
