data = [1,2,4,5]

def count(data):
    if not data:
        return 0
    return 1 + count(data[1:])

print(f"Count: {count(data)}")
