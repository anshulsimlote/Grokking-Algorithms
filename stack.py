print("Stack Implementation")

stack = []

def push(item):
    """Push an item onto the stack."""
    stack.append(item)

def pop():
    """Pop the top item from the stack. Returns None if stack is empty."""
    if not stack:
        print("Stack Underflow! Cannot pop from empty stack.")
        return None
    return stack.pop()

def top():
    """Return the top item without removing it. Returns None if stack is empty."""
    if not stack:
        print("Stack is empty! No top element.")
        return None
    return stack[-1]

def is_empty():
    """Check if the stack is empty."""
    return len(stack) == 0

def size():
    """Return the number of items in the stack."""
    return len(stack)


# Example usage
push(1)
push(2)
push(3)
push(4)

print(f"Stack is: {stack}")
print(f"Popped is: {pop()}")
print(f"Popped is: {pop()}")
print(f"Top is: {top()}")
print(f"Is stack empty? {is_empty()}")
print(f"Stack size: {size()}")
