from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 1. MAP: Square each number in the list
# The lambda function takes x and returns x squared
squares = list(map(lambda x: x**2, numbers))

# 2. FILTER: Keep only numbers greater than 2
# It checks each element and keeps it only if the condition is True
filtered = list(filter(lambda x: x > 2, numbers))

# 3. REDUCE: Calculate the total sum of all numbers
# It combines all elements into a single
total = reduce(lambda x, y: x + y, numbers)

print(f"Original: {numbers}")
print(f"Squared: {squares}")
print(f"Filtered (x > 2): {filtered}")
print(f"Total sum: {total}")