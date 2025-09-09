data = [2, 4, 6]

def sum_list(numbers):
    """Recursively compute the sum of a list."""
    if not numbers:  # cleaner than len(numbers) <= 0
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(f"Recursive Sum: {sum_list(data)}")
